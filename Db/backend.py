import sqlite3
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
    with sqlite3.connect('MODEL/clients.db') as db:
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


def loginUserDb(username, password):
    with sqlite3.connect('users.db') as db:
        con = db.cursor()

    sql = 'SELECT * FROM user WHERE username = ? and password = ?'
    con.execute(sql, [username, password])
    con.fetchall()
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
                'symptom3, symptom4, symptom5) VALUES(?,?,?,?,?,?,?,?,?,?) '
    con.execute(insertSql,
                [first, last, dob, add, zipcode, phone, sym1, sym2, sym3, sym4,
                 sym5])
    db.commit()
    db.close()
