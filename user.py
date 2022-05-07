# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls, data):
        query = 'insert into users (first_name, last_name, email) values ( %(fname)s, %(lname)s, %(email)s);'
        results = connectToMySQL('users').query_db(query, data)
        print(results)
        return results

    @classmethod
    def get_user_by_id(cls, data):
        query = 'select * from users where id = %(id)s;'
        results = connectToMySQL('users').query_db(query, data)
        print(f'results from query {results}')
        return results

    @classmethod
    def update_user(cls, data):
        query = 'update users set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s where id = %(id)s;'
        results = connectToMySQL('users').query_db(query, data)
        print(f'results from update query {results}')
        return results

    # add delete user
    @classmethod
    def delete_user(cls, data):
        query = 'delete from users where id = %(id)s;'
        return connectToMySQL('users').query_db(query, data)
    