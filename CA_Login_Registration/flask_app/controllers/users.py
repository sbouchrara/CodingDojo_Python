# ** import the class from user.py **
# from user import User
# app = Flask(__name__)

from flask_app import app
from flask import Flask, render_template, request,redirect, session
from flask_app.models.user import User

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.form

    if User.validate_register(data):
        User.create(data)
        return redirect('/dashboard')

    return redirect('/')

@app.route("/login", methods=["POST"])
def login():
    data = request.form
    if User.validate_login(data):
        session['logged_email'] = data['email']
        return redirect('/dashboard')
    
    return redirect('/')

@app.route("/dashboard")
def dashboard_page():
    if not 'logged_email' in session:
        return redirect('/')
    return render_template("dashboard.html")

    