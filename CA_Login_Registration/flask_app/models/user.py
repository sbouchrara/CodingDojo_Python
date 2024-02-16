# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask import flash, session
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# REGISTRING NEW USERS (CREATE)
    @classmethod
    def create(cls,data):
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        data = dict(data)
        data['password'] = encrypted_password

        query = """
                    INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) 
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
                """
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DB).query_db(query, data)

# Now we use class methods to query our database
    # GET ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append(cls(user))
        return users



# Static Method to validate registration
    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)

        if len(data['first_name'])<=2:
            flash("First name must be longer than 2 characters!")
            is_valid = False
        if len(data['last_name'])<=2:
            flash("Last name must be longer than 2 characters!")
            is_valid = False
        if len(data['password'])<=8:
            flash("Password must be longer than 8 characters!")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords must match!")
            is_valid = False   
        if not EMAIL_REGEX.match(data['email']): # test whether a field matches the pattern
            flash("Invalid email address!")
            is_valid = False
        if user_in_db:
            flash("Email address already exist!")
            is_valid = False    
        return is_valid
    
    @staticmethod
    def validate_login(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid Email!")
            is_valid = False
        if not user_in_db:
            flash("No user with this email exists!")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Incorrect Password")
            is_valid = False
        
        if is_valid:
            session['logged_name'] = user_in_db.first_name
        else:
            session['error'] = "login"
        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DB).query_db(query,data)
        if result : #result not empty ==> exist on database
            return cls(result[0])
        
        return False    # result is empty ==> does not exist on database    
