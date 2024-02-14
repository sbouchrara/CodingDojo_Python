# ** import the class from ninja.py **
# from ninja import Ninja
# app = Flask(__name__)

from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect, flash
from flask_app.config.mysqlconnection import connectToMySQL,DB

@app.route("/ninjas/new/<int:id>")
def display_listninjas(id):
    data = {
        'id': id
    }
    ninjas = Ninja.get_by_dojo_id(data)
    
    if ninjas != []:
        return render_template("ninja.html", all_ninjas =ninjas)
    else:
        flash("Dojo without ninjas associated")
        return redirect('/')
    
@app.route("/ninjas/new")
def display_ninjapage():
    query = "SELECT * FROM dojos;"
    # make sure to call the connectToMySQL function with the schema you are targeting.
    result = connectToMySQL(DB).query_db(query)
    return render_template("new_ninja.html", ninja_dojos =result)

@app.route("/ninjas/create", methods=["POST"])
def create_ninja():
    # ** Get The DATA From The request.form **
    data = request.form
    
    # print(data['dojo_id'])
    id_Dojo = request.form['dojo_id']
    # ** We pass the data dictionary into the create method from the Friend class. **
    Ninja.create(data)
    
    # ** Don't forget to redirect after saving to the database. **
    return redirect(f"/ninjas/new/{id_Dojo}")