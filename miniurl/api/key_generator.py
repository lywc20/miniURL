import secrets
from instance.settings import Config
from datetime import datetime
from pymongo import MongoClient

class KeyGenerator:
    def __init__(self,pymongo_instance):
        self.client = pymongo_instance

    # Generates shortened urls
    def generateKey(self):
        string = secrets.token_urlsafe(4)
        while not self.available(string):
            string = secrets.token_urlsafe(4)
        return string


    # Checks if URL if shortened URL is available
    def available(self,string):
        if self.client.db.collection.find_one({'shorten_url':string}):
            return False
        return True

    # Binds the shortened URL to the original URL
    def bindUrl(self,short_url,url):
        self.client.db.collection.insert_one({
            'url' : url,
            'shorten_url' : short_url,
            'creation_date' : datetime.utcnow(),
            'expiration' : None
        })

    # Finds shortened url and returns if it exists
    def findUrl(self,short_url):
        res =  self.client.db.collection.find_one({'shorten_url':short_url},{'url':1,'_id':0})
        return res