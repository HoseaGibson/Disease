from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


class LoginWindow:
    def __init__(self, master):
        # Window
        self.master = master
        self.master.title('Login')
        self.master.geometry('500x400')
        # Define varaiables
        self.userText = StringVar
        self.passText = StringVar
        # Label for username and password
        self.loginUsernameLabel = Label(self.master, text='Username', font=('bold', 14), pady=25, padx=200)
        self.loginUsernameLabel.grid(row=0, column=2)
        self.loginPasswordLabel = Label(self.master, text='Password', font=('bold', 14), pady=25)
        self.loginPasswordLabel.grid(row=2, column=2)
        # Entry for username and password
        self.loginUsernameEntry = Entry(self.master, textvariable=self.userText, width=20)
        self.loginUsernameEntry.grid(row=1, column=2)
        self.loginPasswordEntry = Entry(self.master, textvariable=self.passText, width=20)
        self.loginPasswordEntry.grid(row=3, column=2)


def main():
    root = Tk()
    LoginWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
