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

