from flask_app.config.mysqlconnection import connectToMySQL,DB

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
        
    # GET ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of users with cls.
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    # GET BY ID
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        dojo = None
        if result != []:
            dojo = cls(result[0])
        
        return dojo

    # INSERT DATA (CREATE)
    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DB).query_db(query, data)
    
    # MODIFY DATA (UPDATE)
    @classmethod
    def update(cls,data):
        query = """UPDATE dojos 
                SET name=%(name)s,updated_at=NOW() 
                WHERE id = %(id)s;"""
        return connectToMySQL(DB).query_db(query,data)
    
    # DELETE DATA (DELETE)
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)