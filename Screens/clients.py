from tkinter import *
from tkinter import messagebox as ms

from Db.backend import clientTableDb, insertPatient

from symptomsDisease.information import Info

clientTableDb()


class client:
    def __init__(self):
        self.masterClients = Tk()
        self.masterClients.title('Login')
        self.masterClients.geometry('1400x700')
        # Define varaiables
        self.firstnameText = StringVar()
        self.lastnameText = StringVar()
        self.dateOfBirthText = StringVar()
        self.addressText = StringVar()
        self.zipCode = StringVar()
        self.phone = StringVar()
        self.symptom1 = StringVar()
        self.symptom2 = StringVar()
        self.symptom3 = StringVar()
        self.symptom4 = StringVar()
        self.symptom5 = StringVar()
        # Label for first name, last name, dob, address, zip, phone
        self.firstLabel = Label(self.masterClients, text='First Name*', font=('bold', 14), pady=25, padx=10)
        self.firstLabel.grid(row=0, column=0)
        self.lastLabel = Label(self.masterClients, text='Last Name*', font=('bold', 14), pady=25)
        self.lastLabel.grid(row=1, column=0)
        self.dobLabel = Label(self.masterClients, text='Dob*', font=('bold', 14), pady=25, padx=10)
        self.dobLabel.grid(row=2, column=0)
        self.addLabel = Label(self.masterClients, text='Address*', font=('bold', 14), pady=25)
        self.addLabel.grid(row=3, column=0)
        self.zipLabel = Label(self.masterClients, text='Postal*', font=('bold', 14), pady=25)
        self.zipLabel.grid(row=4, column=0)
        self.phoneNumLabel = Label(self.masterClients, text='Phone*', font=('bold', 14), pady=25)
        self.phoneNumLabel.grid(row=5, column=0)
        # Label for 5 symptoms
        self.sym1Label = Label(self.masterClients, text='Symptom 1*', font=('bold', 14), pady=25, padx=60)
        self.sym1Label.grid(row=0, column=2)
        self.sym2Label = Label(self.masterClients, text='Symptom 2*', font=('bold', 14), pady=25)
        self.sym2Label.grid(row=1, column=2)
        self.sym3Label = Label(self.masterClients, text='Symptom 3*', font=('bold', 14), pady=25, padx=10)
        self.sym3Label.grid(row=2, column=2)
        self.sym4Label = Label(self.masterClients, text='Symptom 4*', font=('bold', 14), pady=25)
        self.sym4Label.grid(row=3, column=2)
        self.sym5Label = Label(self.masterClients, text='Symptom 5*', font=('bold', 14), pady=25)
        self.sym5Label.grid(row=4, column=2)

        # Entry for first name, last name, dob, address, zip, phone
        self.firstEntry = Entry(self.masterClients, textvariable=self.firstnameText, width=20)
        self.firstEntry.grid(row=0, column=1)
        self.lastEntry = Entry(self.masterClients, textvariable=self.lastnameText, width=20)
        self.lastEntry.grid(row=1, column=1)
        self.dobEntry = Entry(self.masterClients, textvariable=self.dateOfBirthText, width=20)
        self.dobEntry.grid(row=2, column=1)
        self.addressEntry = Entry(self.masterClients, textvariable=self.addressText, width=20)
        self.addressEntry.grid(row=3, column=1)
        self.zipEntry = Entry(self.masterClients, textvariable=self.zipCode, width=20)
        self.zipEntry.grid(row=4, column=1)
        self.phoneEntry = Entry(self.masterClients, textvariable=self.phone, width=20)
        self.phoneEntry.grid(row=5, column=1)
        # Entry for 5 symptoms
        self.sym1Entry = Entry(self.masterClients, textvariable=self.symptom1, width=20)
        self.sym1Entry.grid(row=0, column=3)
        self.sym2Entry = Entry(self.masterClients, textvariable=self.symptom2, width=20)
        self.sym2Entry.grid(row=1, column=3)
        self.sym3Entry = Entry(self.masterClients, textvariable=self.symptom3, width=20)
        self.sym3Entry.grid(row=2, column=3)
        self.sym4Entry = Entry(self.masterClients, textvariable=self.symptom4, width=20)
        self.sym4Entry.grid(row=3, column=3)
        self.sym5Entry = Entry(self.masterClients, textvariable=self.symptom5, width=20)
        self.sym5Entry.grid(row=4, column=3)
        # Button for saving new user or cancel and return back to login
        self.saveBtn = Button(self.masterClients, text='Save', width=12, bg='skyblue', command=self.insert)
        self.saveBtn.grid(row=6, column=0, pady=12)
        self.viewBtn = Button(self.masterClients, text="View Patients", width=12, command=self.gotoSearch,
                              bg="blue", fg="white")
        self.viewBtn.grid(row=6, column=1)
        self.cancelBtn = Button(self.masterClients, text='Exit', width=12, bg='gray', command=self.returnLoginScreen)
        self.cancelBtn.grid(row=6, column=2)

        # Declare options so and sort items in order
        self.symptomList = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
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
                            'polyuria', 'family_history', 'mucoid_sputum',
                            'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
                            'receiving_blood_transfusion',
                            'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
                            'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum',
                            'prominent_veins_on_calf',
                            'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
                            'skin_peeling',
                            'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
                            'red_sore_around_nose',
                            'yellow_crust_ooze']

        self.symptom1.set(None)
        self.symptom2.set(None)
        self.symptom3.set(None)
        self.symptom4.set(None)
        self.symptom5.set(None)

        self.OPTIONS = sorted(self.symptomList)

        # Entries for symptoms that can be selected in menu
        self.patientSym1Entry = OptionMenu(self.masterClients, self.symptom1, *self.OPTIONS)
        self.patientSym1Entry.grid(row=0, column=4)
        self.patientSym2Entry = OptionMenu(self.masterClients, self.symptom2, *self.OPTIONS)
        self.patientSym2Entry.grid(row=1, column=4)
        self.patientSym3Entry = OptionMenu(self.masterClients, self.symptom3, *self.OPTIONS)
        self.patientSym3Entry.grid(row=2, column=4)
        self.patientSym4Entry = OptionMenu(self.masterClients, self.symptom4, *self.OPTIONS)
        self.patientSym4Entry.grid(row=3, column=4)
        self.patientSym5Entry = OptionMenu(self.masterClients, self.symptom5, *self.OPTIONS)
        self.patientSym5Entry.grid(row=4, column=4)

        # Buttons for Results of each algorithm
        self.randomBtn = Button(self.masterClients, text="Random Forest", width=16, height=2,
                                command=self.randomBtnResults,bg="green", fg="yellow")
        self.randomBtn.grid(row=0, column=6, padx=10)
        self.decisionBtn = Button(self.masterClients, text="Decision Tree", width=16, height=2,
                                  command=self.decisionBtnResults, bg="green", fg="yellow")
        self.decisionBtn.grid(row=1, column=6, padx=10)
        self.bayesBtn = Button(self.masterClients, text="Naive Bayes", width=16, height=2, command=self.bayesBtnResults,
                               bg="green", fg="yellow")
        self.bayesBtn.grid(row=2, column=6, padx=10)
        self.accResultBtn = Button(self.masterClients, text="VIEW ACCURACY PERSONNEL ONLY", width=30, height=2,
                                   command=self.graphingInfo, bg="red", fg="white")
        self.accResultBtn.grid(row=6, column=4, padx=10)


        self.randomLabel = Label(self.masterClients, text="Random Forest", fg="white", bg="red")
        self.randomLabel.grid(row=0, column=5, padx=10, pady=30, sticky=W)
        self.decisionLabel = Label(self.masterClients, text="Decision Tree", fg="white", bg="red")
        self.decisionLabel.grid(row=1, column=5, padx=10, pady=30, sticky=W)
        self.bayesLabel = Label(self.masterClients, text="Naive Bayes", fg="white", bg="red")
        self.bayesLabel.grid(row=2, column=5, padx=10, pady=30, sticky=W)
        self.masterClients.mainloop()

    def graphingInfo(self):
        g = Info()
        g.graphVis(self.masterClients, self.symptom1, self.symptom2, self.symptom3, self.symptom4, self.symptom5)

    # Function to call the random forest function and display the results
    def randomBtnResults(self):
        a = Info()
        a.randomForest(self.masterClients, self.symptom1, self.symptom2, self.symptom3, self.symptom4,
                       self.symptom5)

    # Function to call the decision tree function and display the results
    def decisionBtnResults(self):
        d = Info()
        d.decisionTree(self.masterClients, self.symptom1, self.symptom2, self.symptom3, self.symptom4,
                       self.symptom5)

    # Function to call the bayes function and display the results
    def bayesBtnResults(self):
        b = Info()
        b.navieBayes(self.masterClients, self.symptom1, self.symptom2, self.symptom3, self.symptom4,
                     self.symptom5)

    def insert(self):

        # Find Existing username if any take proper action
        if self.firstEntry == "":
            ms.showerror('Please enter a first name')
        elif self.lastEntry == "":
            ms.showerror('Please enter a last name')
        elif self.dobEntry == "":
            ms.showerror('Please enter a username')
        elif self.addressEntry == "":
            ms.showerror('Please enter a password')
        elif self.zipEntry == "":
            ms.showerror('Please enter a password')
        elif self.phoneEntry == "":
            ms.showerror('Please enter a password')
        else:
            insertPatient(self.firstEntry.get(), self.lastEntry.get(), self.dobEntry.get(), self.addressEntry.get(),
                          self.zipEntry.get(), self.phoneEntry.get(), self.symptom1.get(), self.symptom2.get(),
                          self.symptom3.get(), self.symptom4.get(), self.symptom5.get())

    def gotoSearch(self):
        self.masterClients.destroy()
        from Screens.searcClient import Search
        Search()

    def returnLoginScreen(self):
        self.masterClients.destroy()
        from Screens.login import LoginWindow
        LoginWindow()
