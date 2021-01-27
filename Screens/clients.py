from tkinter import *
from tkinter import messagebox as ms
from Db.backend import clientTableDb, insertPatient

clientTableDb()


class client:
    def __init__(self):
        self.masterClients = Tk()
        self.masterClients.title('Login')
        self.masterClients.geometry('1350x700')
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
        self.saveBtn = Button(self.masterClients, text='Save', width=12, bg='skyblue', command=self.saveUser)
        self.saveBtn.grid(row=5, column=1, pady=12)
        self.cancelBtn = Button(self.masterClients, text='Cancel', width=12, bg='gray', command=self.loginScreen)
        self.cancelBtn.grid(row=5, column=2, pady=12)
        self.masterClients.mainloop()

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
                          self.zipEntry.get(), self.phoneEntry.get(), self.sym1Entry.get(), self.sym2Entry.get(),
                          self.sym3Entry.get(), self.sym4Entry.get(), self.sym5Entry.get())
