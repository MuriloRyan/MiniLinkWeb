""" dbcollections.py """
from objects import LinkObject, UserObject, HashUtils
from bson import ObjectId
import pymongo

#database.users
class UserCollection:
    def __init__(self,database):
        self.collection = database.get_collection('users')

    def signin(self,data):
        query = self.collection.find_one({'email': data['email']})

        if query:
            return None
        else:
            user_object = UserObject(data)

            self.collection.insert_one(user_object.get_data())
            return True
    
    def login(self,data):
        query = self.collection.find_one({'email': data['email']})

        if query:
            hasher = HashUtils()
            user_salt = query['salt']
            user_hash = query['password']
            
            if hasher.create_with_salt(data['password'].encode('utf-8'),user_salt) == user_hash:

                return query
            return None
        else:
            return None

    def update_link_count(self,data):
        try:
            updated_document = {'$inc': {'links': 1}}
            self.collection.update_one({'_id': data['_id']}, updated_document)

            return True
        except:
            return None

#database.links
class LinkCollection:
    def __init__(self,database):
        self.collection = database.get_collection('links')
        self.user_finder = UserCollection(database)

    def verify(self, url):

        if ObjectId.is_valid(url):
            query = self.collection.find_one({'_id': ObjectId(url)})
        else:
            
            query = self.collection.find_one({'original_link': url})

        if query:
            return {'message': f'Minilink {url} exists', 'owner': query['user_id']}

        return None

    def create(self,url,owner):

        if user_query and not self.verify(url):

            link = LinkObject(url,user_query)

            self.user_finder.update_link_count(user_query)
            self.collection.insert_one(link.create())

            return True
        
        return None
    
    def update_clicks(self, link_id):
        query = self.collection.find_one({'$or': [{'_id': link_id}, {'original_link': link_id}]})

        if query:
            updated_document = {'$inc': {'clicks': 1}}
            self.collection.update_one({'_id': query['_id']}, updated_document)
            return True

        return None
