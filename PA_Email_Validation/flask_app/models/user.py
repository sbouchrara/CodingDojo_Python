# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL,DB
from flask import flash

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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

# INSERT DATA (CREATE)
    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DB).query_db(query, data)

# Static Method to validate data
    @staticmethod
    def validate_user(user):
        print(user)
        is_valid = True
        if len(user['first_name'])==0:
            flash("First name should not be empty")
            is_valid = False
        if len(user['last_name'])==0:
            flash("Last name should not be empty")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): # test whether a field matches the pattern
            flash("Invalid email address!")
            is_valid = False
        # else:
        #     result= []
        #     pemail = user['email']
        #     query = "SELECT * FROM users WHERE email = %s;"
        #     result = connectToMySQL(DB).query_db(query,pemail)
        #     if result != []:
        #         flash("Email address already exist!")
        #         is_valid = False
        return is_valid