from tkinter import *

class Search:
    def __init__(self):
        self.masterSearch = Tk()
        self.masterSearch.title('Login')
        self.masterSearch.geometry('700x400')
        # Define varaiables
        self.firstnameText = StringVar()
        self.lastnameText = StringVar()
        self.idText = StringVar()
        self.firstLabel = Label(self.masterSearch, text='First Name*', font=('bold', 14), pady=25, padx=10)
        self.firstLabel.grid(row=0, column=0)
        self.lastLabel = Label(self.masterSearch, text='Last Name*', font=('bold', 14), pady=25)
        self.lastLabel.grid(row=1, column=0)
        self.dobLabel = Label(self.masterSearch, text='Patient ID*', font=('bold', 14), pady=25, padx=10)
        self.dobLabel.grid(row=2, column=0)
        self.firstEntry = Entry(self.masterSearch, textvariable=self.firstnameText, width=20)
        self.firstEntry.grid(row=0, column=1)
        self.lastEntry = Entry(self.masterSearch, textvariable=self.lastnameText, width=20)
        self.lastEntry.grid(row=1, column=1)
        self.dobEntry = Entry(self.masterSearch, textvariable=self.idText, width=20)
        self.dobEntry.grid(row=2, column=1)

        self.updateBtn = Button(self.masterSearch, text='Update', width=12, bg='skyblue', command=self.saveUser)
        self.updateBtn.grid(row=5, column=3, pady=12)
        self.viewAllBtn = Button(self.masterSearch, text='View All', width=12, bg='gray', command=self.loginScreen)
        self.viewAlllBtn.grid(row=5, column=1, pady=12)
        self.searchBtn = Button(self.masterSearch, text='Search', width=12, bg='gray', command=self.loginScreen)
        self.searchBtn.grid(row=5, column=2, pady=12)
        self.cancelBtn = Button(self.masterSearch, text='Cancel', width=12, bg='gray', command=self.loginScreen)
        self.cancelBtn.grid(row=5, column=4, pady=12)