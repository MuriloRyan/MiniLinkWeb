""" objects.py """
import bcrypt
import secrets
import string

class HashUtils:
    def __init__(self):
        pass

    def create_with_salt(self,password,salt):
        return bcrypt.hashpw(password,salt)

    def create_hash(self,password):
        salt = bcrypt.gensalt()

        return {'password': bcrypt.hashpw(password.encode('utf-8'),salt), 'salt':salt}

class LinkObject:
    def __init__(self,url, owner):
        self.charlist = string.ascii_letters + string.digits
        self.url = url
        self.owner = owner

    def reduce(self, length=8):
        reduced_link = ''.join(secrets.choice(self.charlist) for c in range(length))
        return reduced_link
    
    def create(self,length=8):
        return {
            "user_id": self.owner["_id"],
            "original_link": self.url,
            "minilink": self.reduce(length=length),
            "clicks": 0
        }

class UserObject:
    def __init__(self,data):
        hasher = HashUtils()
        salt_and_password = hasher.create_hash(data['password'])

        self.email = data['email']
        self.username = data['username']
        self.password = salt_and_password['password']
        self.salt = salt_and_password['salt']
        self.links = 0
    
    def get_data(self):
        return vars(self)