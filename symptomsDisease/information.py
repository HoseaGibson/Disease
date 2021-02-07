from tkinter import *

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydot as pydot
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.metrics import accuracy_score as accs
from sklearn.naive_bayes import GaussianNB as nbc
from sklearn.tree import DecisionTreeClassifier as dtc, export_graphviz


class Info:
    def __init__(self):

        self.symptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
                         'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
                         'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
                         'throat_irritation',
                         'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain',
                         'weakness_in_limbs',
                         'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                         'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity',
                         'swollen_legs',
                         'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
                         'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts',
                         'drying_and_tingling_lips',
                         'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck',
                         'swelling_joints',
                         'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
                         'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
                         'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
                         'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body',
                         'belly_pain',
                         'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite',
                         'polyuria',
                         'family_history', 'mucoid_sputum',
                         'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
                         'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                         'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum',
                         'prominent_veins_on_calf',
                         'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
                         'skin_peeling',
                         'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                         'red_sore_around_nose',
                         'yellow_crust_ooze']

        self.diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
                         'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma',
                         'Hypertension',
                         ' Migraine', 'Cervical spondylosis',
                         'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid',
                         'hepatitis A',
                         'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis',
                         'Tuberculosis',
                         'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
                         'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
                         'Osteoarthristis',
                         'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection',
                         'Psoriasis',
                         'Impetigo']

        self.condition = {
            'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9,
                          'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}

        self.newList = []
        for l in range(0, len(self.symptoms)):
            self.newList.append(0)
            #print(self.newList)

        df = pd.read_csv("training.csv")
        df.replace({
            'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9,
                          'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

        self.X = df[self.symptoms]
        self.Y = df[["prognosis"]]
        np.ravel(self.Y)

        tr = pd.read_csv("testing.csv")
        tr.replace({
            'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                          'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8,
                          'Bronchial Asthma': 9,
                          'Hypertension ': 10,
                          'Migraine': 11, 'Cervical spondylosis': 12,
                          'Paralysis (brain hemorrhage)': 13, 'Jaundice': 14, 'Malaria': 15, 'Chicken pox': 16,
                          'Dengue': 17, 'Typhoid': 18, 'hepatitis A': 19,
                          'Hepatitis B': 20, 'Hepatitis C': 21, 'Hepatitis D': 22, 'Hepatitis E': 23,
                          'Alcoholic hepatitis': 24, 'Tuberculosis': 25,
                          'Common Cold': 26, 'Pneumonia': 27, 'Dimorphic hemmorhoids(piles)': 28, 'Heart attack': 29,
                          'Varicose veins': 30, 'Hypothyroidism': 31,
                          'Hyperthyroidism': 32, 'Hypoglycemia': 33, 'Osteoarthristis': 34, 'Arthritis': 35,
                          '(vertigo) Paroymsal  Positional Vertigo': 36, 'Acne': 37, 'Urinary tract infection': 38,
                          'Psoriasis': 39,
                          'Impetigo': 40}}, inplace=True)

        self.XTest = tr[self.symptoms]
        self.YTest = tr[["prognosis"]]
        np.ravel(self.YTest)

    def randomForest(self, screens, sym1, sym2, sym3, sym4, sym5):
        self.randomText = Text(screens, height=1, width=30, bg="orange", fg="black")
        self.randomText.grid(row=0, column=7, padx=10)

        self.randomForestClass = rfc()
        self.randomForestClass = self.randomForestClass.fit(self.X, np.ravel(self.Y))

        # Check the accuracy of the algorithm
        self.YPrediction = self.randomForestClass.predict(self.XTest)
        print(accs(self.YTest, self.YPrediction))
        print(accs(self.YTest, self.YPrediction, normalize=False))
        # PRandom =randomForestClass.decision_path(XTest)
        # print(PRandom)

        self.clientSymp = [sym1.get(), sym2.get(), sym3.get(), sym4.get(), sym5.get()]
        for s in range(0, len(self.symptoms)):
            for t in self.clientSymp:
                if t == self.symptoms[s]:
                    self.newList[s] = 1

        self.inputs = [self.newList]
        self.predictions = self.randomForestClass.predict(self.inputs)
        self.predicted = self.predictions[0]

        self.ans = 'no'
        for a in range(0, len(self.diseases)):
            if self.predicted == a:
                self.ans = 'yes'
                break

        if self.ans == 'yes':
            self.randomText.delete("1.0", END)
            self.randomText.insert(END, self.diseases[a])
        else:
            self.randomText.delete("1.0", END)
            self.randomText.insert(END, "Not Found")

    def decisionTree(self, screens, sym1, sym2, sym3, sym4, sym5):
        self.decisionText = Text(screens, height=1, width=30, bg="orange", fg="black")
        self.decisionText.grid(row=1, column=7, padx=10)

        self.decisionTreeClass = dtc()
        self.decisionTreeClass = self.decisionTreeClass.fit(self.X, self.Y)

        # Check the accuracy of the algorithm
        self.YPrediction = self.decisionTreeClass.predict(self.XTest)
        print(accs(self.YTest, self.YPrediction))
        print(accs(self.YTest, self.YPrediction, normalize=False))

        self.clientSymp = [sym1, sym2, sym3, sym4, sym5]

        for s in range(0, len(self.symptoms)):
            for t in self.clientSymp:
                if t == self.symptoms[s]:
                    self.newList[s] = 1

        self.inputs = [self.newList]
        self.predictions = self.decisionTreeClass.predict(self.inputs)
        self.predicted = self.predictions[0]

        self.ans = 'no'
        for a in range(0, len(self.diseases)):
            if self.predicted == a:
                self.ans = 'yes'
                break

        if self.ans == 'yes':
            self.decisionText.delete("1.0", END)
            self.decisionText.insert(END, self.diseases[a])
        else:
            self.decisionText.delete("1.0", END)
            self.decisionText.insert(END, "Not Found")

    def navieBayes(self, screens, sym1, sym2, sym3, sym4, sym5):
        self.bayesText = Text(screens, height=1, width=30, bg="orange", fg="black")
        self.bayesText.grid(row=2, column=7, padx=10)

        self.bayesClassifier = nbc()
        self.bayesClassifier = self.bayesClassifier.fit(self.X, np.ravel(self.Y))

        # Check the accuracy of the algorithm
        self.YPrediction = self.bayesClassifier.predict(self.XTest)
        print(accs(self.YTest, self.YPrediction))
        print(accs(self.YTest, self.YPrediction, normalize=False))

        self.clientSymp = [sym1, sym2, sym3, sym4, sym5]

        for s in range(0, len(self.symptoms)):
            for t in self.clientSymp:
                if (t == self.symptoms[s]):
                    self.newList[s] = 1

        self.inputs = [self.newList]
        self.predictions = self.bayesClassifier.predict(self.inputs)
        self.predicted = self.predictions[0]

        self.ans = 'no'
        for a in range(0, len(self.diseases)):
            if self.predicted == a:
                self.ans = 'yes'
                break

        if self.ans == 'yes':
            self.bayesText.delete("1.0", END)
            self.bayesText.insert(END, self.diseases[a])
        else:
            self.bayesText.delete("1.0", END)
            self.bayesText.insert(END, "Not Found")

    def graphVis(self, screens, sym1, sym2, sym3, sym4, sym5):
        self.model = rfc(n_estimators=95, random_state=30)
        self.model.fit(self.X, np.ravel(self.Y))

        self.model3 = rfc(n_estimators=95, random_state=30)
        self.model3.fit(self.X, np.ravel(self.Y))

        self.model2 = rfc(n_estimators=10, max_depth=3)
        self.model2.fit(self.X, np.ravel(self.Y))

        self.pred = self.model.predict(self.XTest)
        print(self.pred)

        # Text to show on screen accuracy of random forest
        self.accScore = "Accuracy for Random Forest is ", accs(self.YTest, self.pred)
        # print("Accuracy for Random Forest is " , accs(self.YTest,self.pred))
        self.accText = Label(screens, text=self.accScore)
        self.accText.grid(row=16, column=0, padx=10, pady=10)

        self.features = list(self.X)
        self.featureImport = pd.Series(self.model.feature_importances_, index=self.features)
        self.modelPath = pd.Series(self.model.decision_path(self.X))

        self.modelProb = self.model.predict_proba(self.XTest)

        self.mylist = [sym1.get(), sym2.get(), sym3.get(), sym4.get(), sym5.get()]

        for self.mylist in self.featureImport:
            self.feaImportance = "The feature importance ", self.featureImport
            print(self.featureImport)
        self.importance = Label(screens, text=self.feaImportance)
        self.importance.grid(row=17, column=0, padx=10, pady=10)

        print(self.modelPath)
        print(self.modelProb)

        # Creates a decision tree to see show decision made by random forest classifier
        # Saves in a dot file
        self.tree = self.model.estimators_[2]
        export_graphviz(self.tree, out_file='tree.dot', feature_names=self.features, rounded=True, precision=1)
        (graph,) = pydot.graph_from_dot_file('tree.dot')

        # Creates a smaller decision tree to see show decision made by random forest classifier easier to view
        # Saves in a dot file
        self.tree2 = self.model2.estimators_[2]
        export_graphviz(self.tree2, out_file='tree_small.dot', feature_names=self.features, rounded=True, precision=1)

        (graph,) = pydot.graph_from_dot_file('tree_small.dot')

        plt.style.use('fivethirtyeight')
        self.xValue = list(range(len(self.featureImport)))

        plt.bar(self.xValue, self.featureImport, orientation='vertical')

        plt.xticks(self.xValue, self.model3, rotation='vertical')
        plt.ylabel = 'Importance'
        plt.xlabel = 'Variable'
        plt.title = 'Variable Importance'
        plt.show()

        # creates line graph of importance to list of symptoms total of 95 values passed
        self.xs = np.array(self.features)
        self.ys = self.xValue
        plt.plot(self.xs, self.ys)
        plt.show()
