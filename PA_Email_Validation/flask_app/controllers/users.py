# ** import the class from friend.py **
# from friend import Friend
# app = Flask(__name__)

from flask_app import app
from flask import Flask, render_template, request,redirect, session
from flask_app.models.user import User

@app.route("/")
def read_all():
    # ** call the get all classmethod to get all users **
    users = User.get_all()
    
    return render_template("read_all.html",all_users = users)

@app.route("/create")
def create():
    return render_template("new_user.html")


@app.route("/create/new", methods=["POST"])
def create_user():
    session['first_name']   = request.form['first_name']
    session['last_name']    = request.form['last_name']
    session['email']        = request.form['email']
    # if there are errors:
    # We call the staticmethod on user model to validate
    if not User.validate_user(request.form):
        
        return render_template("user.html",first_name_on_template=session['first_name'], 
        last_name_on_template=session['last_name'], email_on_template=session['email'])
    else:
        # else no errors: ** Get The DATA From The request.form **
        data = request.form
    
        # ** We pass the data dictionary into the create method from the Friend class. **
        User.create(data)
    
        # ** Don't forget to redirect after saving to the database. **
        return redirect('/')
        # redirect to the route where the user form is rendered.
        # return redirect("/create")

    