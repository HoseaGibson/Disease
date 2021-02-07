from tkinter import *
from tkinter import messagebox as ms

from Db.backend import addUserAccountDb


class accounts:

    def __init__(self):
        self.masterAcc = Tk()
        self.masterAcc.title('Login')
        self.masterAcc.geometry('600x400')
        # Define varaiables
        self.firstnameText = StringVar()
        self.lastnameText = StringVar()
        self.userText = StringVar()
        self.passText = StringVar()
        # Label for first name, last name, username and password
        self.firstLabel = Label(self.masterAcc, text='First Name*', font=('bold', 14), pady=25, padx=10)
        self.firstLabel.grid(row=0, column=0)
        self.lastLabel = Label(self.masterAcc, text='Last Name*', font=('bold', 14), pady=25)
        self.lastLabel.grid(row=1, column=0)
        self.usernameLabel = Label(self.masterAcc, text='Username*', font=('bold', 14), pady=25, padx=10)
        self.usernameLabel.grid(row=2, column=0)
        self.passwordLabel = Label(self.masterAcc, text='Password*', font=('bold', 14), pady=25)
        self.passwordLabel.grid(row=3, column=0)
        # Entry for first name, last name, username and password
        self.firstEntry = Entry(self.masterAcc, textvariable=self.firstnameText, width=20)
        self.firstEntry.grid(row=0, column=1)
        self.lastEntry = Entry(self.masterAcc, textvariable=self.lastnameText, width=20)
        self.lastEntry.grid(row=1, column=1)
        self.usernameEntry = Entry(self.masterAcc, textvariable=self.userText, width=20)
        self.usernameEntry.grid(row=2, column=1)
        self.passwordEntry = Entry(self.masterAcc, textvariable=self.passText, width=20)
        self.passwordEntry.grid(row=3, column=1)
        # Button for saving new user or cancel and return back to login
        self.saveBtn = Button(self.masterAcc, text='Save', width=12, bg='skyblue', command=self.saveUser)
        self.saveBtn.grid(row=5, column=1, pady=12)
        self.cancelBtn = Button(self.masterAcc, text='Cancel', width=12, bg='gray', command=self.returnLoginScreen)
        self.cancelBtn.grid(row=5, column=2, pady=12)
        self.masterAcc.mainloop()

    def saveUser(self):

        if self.firstEntry == "":
            ms.showerror('Please enter a first name')
        elif self.lastEntry == "":
            ms.showerror('Please enter a last name')
        elif self.usernameEntry == "":
            ms.showerror('Please enter a username')
        elif self.passwordEntry == "":
            ms.showerror('Please enter a password')
        else:
            addUserAccountDb(self.firstEntry.get(), self.lastEntry.get(), self.usernameEntry.get(),
                             self.passwordEntry.get())
            self.returnLoginScreen()


    def returnLoginScreen(self):
        self.masterAcc.destroy()
        from Screens.login import LoginWindow
        LoginWindow()
