import sqlite3
from flask import session
import werkzeug
connection = sqlite3.connect('users.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Users (
login TEXT NOT NULL,
password TEXT NOT NULL,
accesscode TEXT NOT NULL
)
''')
connection.commit()

def takeuser(log,passw,accesscode):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[0]==log and user[1]==passw and user[2]==accesscode:
            return True
    return False

def checkexist(usname):
    connection = sqlite3.connect('users.db', check_same_thread=False)
    cursor = connection.cursor()
    userlist = []
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user[0] == usname:
            return True
    return False

def createuser(log,passw,accesscode):
    if checkexist(log)==True:
        return "Логин занят"
    else:
        cursor.execute(
            'INSERT INTO Users (login, password, accesscode) VALUES (?, ?, ?)',
            (log,passw,accesscode))
        connection.commit()
