# ** import the class from friend.py **
# from friend import Friend
# app = Flask(__name__)

from flask_app import app
from flask import Flask, render_template, request,redirect
from flask_app.models.user import User

@app.route("/")
def read_all():
    # ** call the get all classmethod to get all users **
    users = User.get_all()
    print("--------------------")
    print(users)
    print("--------------------")
    return render_template("read_all.html",all_users = users)

@app.route("/create")
def create():
    return render_template("new_user.html")


@app.route("/create/new", methods=["POST"])
def create_user():
    # ** Get The DATA From The request.form **
    data = request.form
    print("----------create user----------------")
    print(data)
    print("---------Printed Data----------------")
    # ** We pass the data dictionary into the create method from the Friend class. **
    User.create(data)
    
    # ** Don't forget to redirect after saving to the database. **
    return redirect('/')