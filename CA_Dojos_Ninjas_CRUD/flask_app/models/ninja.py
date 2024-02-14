from flask_app.models.dojo import Dojo
from flask_app.config.mysqlconnection import connectToMySQL,DB

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None
    
    # GET Ninja BY ID
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)

        # Initialize the attributes of the ninja instance (Using constructor)
        ninja = None
        if result != []:
            # Create an instance of the dojo Class
            dojo_data = {
                'id': result[0]['dojos.id'],
                'name': result[0]['name'],
                'created_at': result[0]['dojos.created_at'],
                'updated_at': result[0]['dojos.updated_at'],
            }
            # Set the dojo attribute of the ninja instance equal to the dojo instance
            dojo = Dojo(dojo_data)
            ninja = cls(result[0])
            ninja.dojo = dojo
        return ninja
    
    @classmethod
    def get_by_dojo_id(cls,data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        # Initialize the attributes of the ninja instance (Using constructor)
        ninjas = []
        for item in result :
            # Create an instance of the dojo Class
            dojo_data = {
                'id': result[0]['dojos.id'],
                'name': result[0]['name'],
                'created_at': result[0]['dojos.created_at'],
                'updated_at': result[0]['dojos.updated_at'],
            }
            ninja = cls(item)
            ninja.dojo = Dojo(dojo_data)
            ninjas.append(ninja)
        return ninjas
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id;"
        result = connectToMySQL(DB).query_db(query)

        # Initialize the attributes of the ninja instance (Using constructor)
        ninjas = []
        for item in result :
            # Create an instance of the dojo Class
            dojo_data = {
                'id': result[0]['dojos.id'],
                'name': result[0]['name'],
                'created_at': result[0]['dojos.created_at'],
                'updated_at': result[0]['dojos.updated_at'],
            }
            ninja = cls(item)
            ninja.dojo = Dojo(dojo_data)
            ninjas.append(ninja)
        return ninjas
    
    @classmethod
    def create(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);" 
        return connectToMySQL(DB).query_db(query, data) # return the ID of the new created raw
    
    @classmethod
    def update(cls,data):
        query ="UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, updated_at = NOW(), dojo_id = %(dojo_id)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data) # return True (if the UPDATE happened sucessfully) or False
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data) # return True (if the DELETE happened sucessfully) or False