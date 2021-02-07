import sqlite3
from tkinter import *

from tkinter import messagebox as ms


def createUserDb():
    with sqlite3.connect('users.db') as db:
        c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS user (firstname TEXT NOT NULL,
                  lastname TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL);""")
    db.commit()
    db.close()


def clientTableDb():
    with sqlite3.connect('clients.db') as db:
        c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS client(firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL,
                    birthdate TEXT NOT NULL,
                    address TEXT NOT NULL,
                    postal TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    symptom1 TEXT NOT NULL,
                    symptom2 TEXT NOT NULL,
                    symptom3 TEXT NOT NULL,
                    symptom4 TEXT NOT NULL,
                    symptom5 TEXT NOT NULL);""")
    db.commit()
    db.close()


def loginUserDb(username, password, clear1, clear2, screen):
    from Screens.clients import client
    with sqlite3.connect('users.db') as db:
        con = db.cursor()

    u = username
    p = password

    sql = 'SELECT * FROM user WHERE username = ? and password = ?'
    con.execute(sql, [username, password])
    results = con.fetchall()

    if u == "" or p == "":
        ms.showwarning('All entries with (*) are required ')
    if results:
        clear1.delete(0, END)
        clear2.delete(0, END)
        screen.destroy()
        client()

    else:
        ms.showerror('Credentials incorrect')
    db.commit()
    db.close()


def addUserAccountDb(first, last, username, password):
    with sqlite3.connect('users.db') as db:
        con = db.cursor()

        findsql = 'SELECT username FROM user WHERE username = ?'
        con.execute(findsql, [username])
        f = con.fetchall()
        if f:
            ms.showerror('Account Exist')

        else:
            ms.showinfo('Account Created')
        insertSql = 'INSERT INTO user(firstname, lastname, username, password) VALUES(?,?,?,?)'
        con.execute(insertSql, [first, last, username, password])
        db.commit()


def insertPatient(first, last, dob, add, zipcode, phone, sym1, sym2, sym3, sym4, sym5):
    with sqlite3.connect('clients.db') as db:
        con = db.cursor()

    findSql = 'SELECT firstname, lastname FROM client WHERE firstname =? and lastname=? '
    con.execute(findSql, [first, last])
    f = con.fetchall()
    if f:
        ms.showerror('User already exist')
    insertSql = 'INSERT INTO client(firstname, lastname, birthdate, address, postal, phone, symptom1, symptom2, ' \
                'symptom3, symptom4, symptom5) VALUES(?,?,?,?,?,?,?,?,?,?,?) '
    con.execute(insertSql, [first, last, dob, add, zipcode, phone, sym1, sym2, sym3, sym4, sym5])
    db.commit()
    db.close()


def viewAll(screen):
    with sqlite3.connect('clients.db') as db:
        con = db.cursor()
    sql = 'SELECT *, oid FROM client'
    con.execute(sql)
    records = con.fetchall()
    printRd = ""
    for record in records:
        printRd += str(record) + "\n"
        # printRd += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(
        # record[4]) + " " + str(record[5]) + " " + str(record[6]) + " " + str(record[7]) + " " + str(
        # record[8]) + " " + str(record[9]) + " " + str(record[10]) + " " + str(record[11]) + '\n'
        queryViewLabel = Label(screen, text=printRd)

        queryViewLabel.grid(row=8, column=0, columnspan=2)

    db.commit()
    db.close()


def searchIndividualQuery(first, last, screen):
    with sqlite3.connect('clients.db') as db:
        con = db.cursor()
    if first == "" or last == "":
        errorMess = Label(screen, text="Please enter a name and last name")
        errorMess.grid(row=10, column=0, padx=10, sticky=W)
    else:
        sql = 'SELECT * FROM client WHERE firstname = ? and lastname = ?'
        con.execute(sql, [(first), (last)])
        records = con.fetchall()
        printSearch = ""

        for recs in records:
            printSearch += str(recs[0]) + " " + str(recs[1]) + " " + str(recs[2]) + " " + str(recs[3]) + " " + str(
                recs[4]) + " " + str(recs[5]) + " " + str(recs[6]) + " " + str(recs[7]) + " " + str(
                recs[8]) + " " + str(recs[9]) + " " + str(recs[10]) + '\n'
        querySearchLabel = Label(screen, text=printSearch)
        querySearchLabel.grid(row=10, column=0, columnspan=2)

    db.commit()
    db.close()
