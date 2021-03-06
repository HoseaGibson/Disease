from tkinter import *
from Db.backend import createUserDb, loginUserDb
from Screens.account import accounts

createUserDb()


class LoginWindow:
    def __init__(self):
        # Window
        self.master = Tk()
        self.master.title('Login')
        self.master.geometry('400x300')
        # Define varaiables
        self.userText = StringVar()
        self.passText = StringVar()
        # Label for username and password
        self.loginUsernameLabel = Label(self.master, text='Username', font=('bold', 14), pady=25, padx=10)
        self.loginUsernameLabel.grid(row=0, column=0)
        self.loginPasswordLabel = Label(self.master, text='Password', font=('bold', 14), pady=25)
        self.loginPasswordLabel.grid(row=1, column=0)
        # Entry for username and password
        self.loginUsernameEntry = Entry(self.master, textvariable=self.userText, width=20)
        self.loginUsernameEntry.grid(row=0, column=1)
        self.loginPasswordEntry = Entry(self.master, textvariable=self.passText, width=20)
        self.loginPasswordEntry.grid(row=1, column=1)
        # Button for login or create new user
        self.loginBtn = Button(self.master, text='Login', width=12, bg='skyblue', command=self.login)
        self.loginBtn.grid(row=5, column=1, pady=12)
        self.createBtn = Button(self.master, text='Create Account', width=12, bg='gray', command=self.createAcc)
        self.createBtn.grid(row=5, column=2, pady=12)
        self.master.mainloop()

    def login(self):
        self.user = self.userText
        self.passW = self.passText
        self.clearUser = self.loginUsernameEntry
        self.clearPass = self.loginPasswordEntry
        loginUserDb(self.user.get(), self.passW.get(), self.loginUsernameEntry, self.loginPasswordEntry, self.master)

    def createAcc(self):
        self.master.destroy()
        accounts()


LoginWindow()
