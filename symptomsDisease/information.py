import graphviz as graphviz
import pandas as pd
import numpy as np
from tkinter import *
from sklearn.metrics import accuracy_score as accs
from sklearn.ensemble import RandomForestClassifier as rfc, RandomForestRegressor
from sklearn.naive_bayes import GaussianNB as nbc
from sklearn.tree import DecisionTreeClassifier as dtc, export_graphviz
from sklearn import tree
import pydot as pydot
import matplotlib.pyplot as plt

symptoms = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
            'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
            'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
            'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
            'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
            'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
            'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
            'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
            'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
            'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
            'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
            'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
            'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
            'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
            'family_history', 'mucoid_sputum',
            'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
            'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
            'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf',
            'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
            'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose',
            'yellow_crust_ooze']

diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
            'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension',
            ' Migraine', 'Cervical spondylosis',
            'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
            'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis',
            'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
            'Heartattack', 'Varicoseveins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthristis',
            'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne', 'Urinary tract infection', 'Psoriasis',
            'Impetigo']

condition = {'prognosis': {'Fungal infection': 0, 'Allergy': 1, 'GERD': 2, 'Chronic cholestasis': 3, 'Drug Reaction': 4,
                      'Peptic ulcer diseae': 5, 'AIDS': 6, 'Diabetes ': 7, 'Gastroenteritis': 8, 'Bronchial Asthma': 9,
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

newList = []
for l in range(0, len(symptoms)):
    newList.append(0)
    print(newList)

df = pd.read_csv("testing.csv")
df.replace(condition, inplace=True)

X = df[symptoms]
Y = df[[condition]]
np.ravel(Y)

tr = pd.read_csv("testing.csv")
tr.replace(condition, inplace=True)

XTest = tr[symptoms]
YTest = tr[[condition]]
np.ravel(YTest)


def randomForest(screens, sym1, sym2, sym3, sym4, sym5):
    randomText = Text(screens, height=1, width=40, bg="orange", fg="black")
    randomText.grid(row=13, column=1, padx=10)

    randomForestClass = rfc()
    randomForestClass = randomForestClass.fit(X, np.ravel(Y))

    # Check the accuracy of the algorithm
    YPrediction = randomForestClass.predict(XTest)
    print(accs(YTest, YPrediction))
    print(accs(YTest, YPrediction, normalize=False))
    #PRandom =randomForestClass.decision_path(XTest)
    #print(PRandom)

    clientSymp = [sym1.get(), sym2.get(), sym3.get(), sym4.get(), sym5.get()]
    for s in range(0, len(symptoms)):
        for t in clientSymp:
            if t == symptoms[s]:
                newList[s] = 1

    input = [newList]
    predictions =randomForestClass.predict(input)
    predicted = predictions[0]

    ans = 'no'
    for a in range(0, len(diseases)):
        if predicted == a:
            ans = 'yes'
            break

    if ans == 'yes':
        randomText.delete("1.0", END)
        randomText.insert(END, diseases[a])
    else:
        randomText.delete("1.0", END)
        randomText.insert(END, "Not Found")

def decisionTree( screens, sym1, sym2, sym3, sym4, sym5):

        decisionText = Text(screens, height=1, width=40, bg="orange", fg="black")
        decisionText.grid(row=14, column=1, padx=10)

        decisionTreeClass = dtc()
        decisionTreeClass = decisionTreeClass.fit(X,Y)

        # Check the accuracy of the algorithm
        YPrediction = decisionTreeClass.predict(XTest)
        print(accs(YTest, YPrediction))
        print(accs(YTest, YPrediction, normalize=False))

        clientSymp = [sym1,sym2,sym3,sym4,sym5]

        for s in range(0,len(symptoms)):
            for t in clientSymp:
                if t==symptoms[s]:
                   newList[s]=1

        input = [newList]
        predictions = decisionTreeClass.predict(input)
        predicted=predictions[0]

        ans = 'no'
        for a in range(0,len(diseases)):
            if predicted == a:
                ans = 'yes'
                break

        if ans == 'yes':
            decisionText.delete("1.0", END)
            decisionText.insert(END, diseases[a])
        else:
           decisionText.delete("1.0", END)
           decisionText.insert(END, "Not Found")

def navieBayes(screens, sym1, sym2, sym3, sym4, sym5):

        bayesText = Text(screens, height=1, width=40, bg="orange", fg="black")
        bayesText.grid(row=15, column=1, padx=10)

        bayesClassifier = nbc()
        bayesClassifier = bayesClassifier.fit(X,np.ravel(Y))

        # Check the accuracy of the algorithm
        YPrediction = bayesClassifier.predict(XTest)
        print(accs(YTest, YPrediction))
        print(accs(YTest, YPrediction, normalize=False))

        clientSymp = [sym1,sym2,sym3,sym4,sym5]

        for s in range(0,len(symptoms)):
            for t in clientSymp:
                if(t==symptoms[s]):
                    newList[s]=1

        input = [newList]
        predictions = bayesClassifier.predict(input)
        predicted=predictions[0]

        ans = 'no'
        for a in range(0,len(diseases)):
            if predicted == a:
                ans = 'yes'
                break

        if ans == 'yes':
            bayesText.delete("1.0", END)
            bayesText.insert(END,diseases[a])
        else:
            bayesText.delete("1.0", END)
            bayesText.insert(END, "Not Found")

def graphVis(screens,sym1, sym2, sym3, sym4, sym5):

        model = rfc(n_estimators=95, random_state=30)
        model.fit(X,np.ravel(Y))

        model3 = rfc(n_estimators=95, random_state=30)
        model3.fit(X,np.ravel(Y))

        model2 = rfc(n_estimators=10, max_depth=3)
        model2.fit(X,np.ravel(Y))

        pred = model.predict(XTest)
        print(pred)

        # Text to show on screen accuracy of random forest
        accScore = "Accuracy for Random Forest is " , accs(YTest,pred)
        #print("Accuracy for Random Forest is " , accs(self.YTest,self.pred))
        accText = Label(screens, text= accScore)
        accText.grid(row=16, column=0, padx=10, pady=10)

        features = list(X)
        featureImport = pd.Series(model.feature_importances_, index=features)
        modelPath = pd.Series(model.decision_path(X))
        modelProb= model.predict_proba(XTest)

        mylist= [sym1.get(),sym2.get(),sym3.get(),sym4.get(),sym5.get()]

        for mylist in featureImport:
            feaImportance = "The feature importance ", featureImport
            print(featureImport)
        importance = Label(screens,text= feaImportance)
        importance.grid(row=17, column=0, padx=10, pady=10)

        print(modelPath)
        print(modelProb)

        # Creates a decision tree to see show decision made by random forest classifier
        # Saves in a dot file
        tree = model.estimators_[2]
        export_graphviz(tree, out_file='tree.dot', feature_names=features, rounded=True, precision=1)
        (graph, ) = pydot.graph_from_dot_file('tree.dot')

        # Creates a smaller decision tree to see show decision made by random forest classifier easier to view
        # Saves in a dot file
        tree2 =model2.estimators_[2]
        export_graphviz(tree2, out_file='tree_small.dot', feature_names=features, rounded=True, precision=1)

        (graph, ) = pydot.graph_from_dot_file('tree_small.dot')

        plt.style.use('fivethirtyeight')
        xValue= list(range(len(featureImport)))

        plt.bar(xValue, featureImport, orientation ='vertical')

        plt.xticks(xValue, model3,rotation='vertical')
        plt.ylabel=('Importance')
        plt.xlabel=('Variable')
        plt.title=('Variable Importance')
        plt.show()

        # creates line graph of importance to list of symptoms total of 95 values passed
        xs= np.array(features)
        ys=  xValue
        plt.plot(xs,ys)
        plt.show()