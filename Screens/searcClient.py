import sqlite3
from tkinter import *

from Db.backend import viewAll, searchIndividualQuery


class Search:
    def __init__(self):
        self.masterSearch = Tk()
        self.masterSearch.title('Login')
        self.masterSearch.geometry('1000x600')
        # Define varaiables
        self.firstnameText = StringVar()
        self.lastnameText = StringVar()
        self.idText = StringVar()
        self.firstLabel = Label(self.masterSearch, text='First Name*', font=('bold', 14), pady=25, padx=10)
        self.firstLabel.grid(row=0, column=0)
        self.lastLabel = Label(self.masterSearch, text='Last Name*', font=('bold', 14), pady=25)
        self.lastLabel.grid(row=1, column=0)
        self.idLabel = Label(self.masterSearch, text='Patient ID*', font=('bold', 14), pady=25, padx=10)
        self.idLabel.grid(row=2, column=0)
        self.firstEntry = Entry(self.masterSearch, textvariable=self.firstnameText, width=20)
        self.firstEntry.grid(row=0, column=1)
        self.lastEntry = Entry(self.masterSearch, textvariable=self.lastnameText, width=20)
        self.lastEntry.grid(row=1, column=1)
        self.idEntry = Entry(self.masterSearch, textvariable=self.idText, width=20)
        self.idEntry.grid(row=2, column=1)

        self.updateBtn = Button(self.masterSearch, text='Update', width=12, bg='skyblue', command=self.updatePatient)
        self.updateBtn.grid(row=2, column=2)
        self.viewAllBtn = Button(self.masterSearch, text='View All', width=12, bg='gray', command=self.viewAllPatients)
        self.viewAllBtn.grid(row=0, column=2)
        self.searchBtn = Button(self.masterSearch, text='Search', width=12, bg='gray', command=self.searchPatient)
        self.searchBtn.grid(row=1, column=2)
        self.exitBtn = Button(self.masterSearch, text='Exit', width=12, bg='gray', command=self.returnLoginScreen)
        self.exitBtn.grid(row=3, column=2, pady=12)

    def viewAllPatients(self):
        viewAll(self.masterSearch)

    def searchPatient(self):
        searchIndividualQuery(self.firstnameText.get(), self.lastnameText.get(), self.masterSearch)

    def returnLoginScreen(self):
        self.masterSearch.destroy()
        from Screens.login import LoginWindow
        LoginWindow()

    def updatePatient(self):
        with sqlite3.connect('clients.db') as db:
            c = db.cursor()

        self.recordId = self.idText.get()
        if self.recordId == "":
            self.errorMess = Label(self.searchPatient(), text="Please enter patient ID")
            self.errorMess.grid(row=10, column=0, padx=10, sticky=W)
        else:
            self.editor = Tk()
            self.editor.geometry('1400x1000')
            self.editor.title('Update Patient')

            sql = 'SELECT * FROM client WHERE oid = ' + self.recordId
            c.execute(sql)
            self.records = c.fetchall()

            # Set labels for patient information
            self.patientFirstName = Label(self.editor, text="Patient Firstname", fg="yellow", bg="black")
            self.patientFirstName.grid(row=6, column=0, padx=10, pady=15, sticky=W)
            self.patientLastName = Label(self.editor, text="Patient Lastname", fg="yellow", bg="black")
            self.patientLastName.grid(row=7, column=0, padx=10, pady=15, sticky=W)
            self.patientDobNum = Label(self.editor, text="Patient DoB", fg="yellow", bg="black")
            self.patientDobNum.grid(row=8, column=0, padx=10, pady=15, sticky=W)
            self.patientAddressName = Label(self.editor, text="Patient Address", fg="yellow", bg="black")
            self.patientAddressName.grid(row=9, column=0, padx=10, pady=15, sticky=W)
            self.patientPostalNum = Label(self.editor, text="Patient Postal", fg="yellow", bg="black")
            self.patientPostalNum.grid(row=10, column=0, padx=10, pady=15, sticky=W)
            self.patientPhoneNum = Label(self.editor, text="Patient Phone Number", fg="yellow", bg="black")
            self.patientPhoneNum.grid(row=11, column=0, padx=10, pady=15, sticky=W)

            # Set entry fields for patient information
            self.patientFirstEntry = Entry(self.editor, width=20)
            self.patientFirstEntry.grid(row=6, column=1)
            self.patientLastEntry = Entry(self.editor, width=20)
            self.patientLastEntry.grid(row=7, column=1)
            self.patientDobEntry = Entry(self.editor, width=20)
            self.patientDobEntry.grid(row=8, column=1)
            self.patientAddressEntry = Entry(self.editor, width=20)
            self.patientAddressEntry.grid(row=9, column=1)
            self.patientPostalEntry = Entry(self.editor, width=20)
            self.patientPostalEntry.grid(row=10, column=1)
            self.patientPhoneEntry = Entry(self.editor, width=20)
            self.patientPhoneEntry.grid(row=11, column=1)

            for recs in self.records:
                self.patientFirstEntry.insert(0, recs[0])
                self.patientLastEntry.insert(0, recs[1])
                self.patientDobEntry.insert(0, recs[2])
                self.patientAddressEntry.insert(0, recs[3])
                self.patientPostalEntry.insert(0, recs[4])
                self.patientPhoneEntry.insert(0, recs[5])

            self.updateBtn = Button(self.editor, text="Update Record",
                                    command=self.updateQuery)
            self.updateBtn.grid(row=12, column=0, columnspan=2, pady=10)

    def updateQuery(self):
        with sqlite3.connect('clients.db') as db:
            c = db.cursor()
        self.recordId = self.idText.get()
        c.execute(""" UPDATE client SET
            firstname = :first,
            lastname = :last,
            birthdate = :dob,
            address = :add,
            postal = :post,
            phone = :number

            WHERE oid = :oid""",
                  {'first': self.patientFirstEntry.get(),
                   'last': self.patientLastEntry.get(),
                   'dob': self.patientDobEntry.get(),
                   'add': self.patientAddressEntry.get(),
                   'post': self.patientPostalEntry.get(),
                   'number': self.patientPhoneEntry.get(),
                   'oid': self.recordId
                   })
        db.commit()
        db.close()
        self.editor.destroy()
