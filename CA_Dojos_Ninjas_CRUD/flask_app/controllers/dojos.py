# ** import the class from dojo.py **
# from dojo import Dojo
# app = Flask(__name__)

from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo

@app.route("/")
def read_all():
    # ** call the get all classmethod to get all users **
    dojos = Dojo.get_all()
    
    # return render_template("read_all.html",all_dojos = dojos)
    return render_template("dojo.html",all_dojos = dojos)

@app.route("/create/new", methods=["POST"])
def create_dojo():
    # ** Get The DATA From The request.form **
    data = request.form
    
    # ** We pass the data dictionary into the create method from the Friend class. **
    Dojo.create(data)
    
    # ** Don't forget to redirect after saving to the database. **
    return redirect('/')