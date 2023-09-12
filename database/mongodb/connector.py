""" connector.py """
from dbcollections import UserCollection, LinkCollection
import pymongo
from os import getenv

mongodb_url = getenv("MONGO_URL")

#facade pattern class
class Database:
    def __init__(self):
        self.Cluster = pymongo.MongoClient(mongodb_url)
        self.database = self.Cluster.get_database('MiniLinkWebDatabase')

        self.user = UserCollection(self.database)
        self.link = LinkCollection(self.database)
    
    def test(self):
        return self.Cluster
