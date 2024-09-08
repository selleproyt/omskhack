from flask import Flask
from flask import request
from flask import render_template, redirect
from base import takeuser
from flask import session
import os
app = Flask(__name__,static_folder="static")
app.config['SECRET_KEY']="5b38897f6f7b7bb3fcb2c8a55027235710df24b1"
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'tiff', 'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def index():
    return render_template('main.html')


@app.route("/lk")
def lk():
    if 'access' in session:
        return render_template('main2.html')
    else:
        return f"Access denied"

@app.route("/submitreg", methods=['POST'])
def submitreg():
    username = request.form["username"]
    password = request.form["password"]
    code = request.form["code"]
    flag=takeuser(username,password,code)
    if flag==True:
        session['access']="accepted"
        return f'<meta http-equiv="refresh" content="1; url=http://localhost:5000/lk">'
    else:
        return f"Access denied."

@app.route("/submitnetwork", methods=['POST'])
def submitnetwork():
    return f"Result:"


app.run()