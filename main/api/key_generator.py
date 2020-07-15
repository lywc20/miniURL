import secrets
from settings import Config
from datetime import datetime
from ..extensions import mongo


# Generates shortened urls
def generateKey():
    string = secrets.token_urlsafe(4)
    while not available(string):
        string = secrets.token_urlsafe(4)
    return string


# Checks if URL if shortened URL is available
def available(string):
     if mongo.db.urls.find_one({'shorten_url':string}):
         return False
     return True

# Binds the shortened URL to the original URL
def bindUrl(short_url,url):
    mongo.db.urls.insert_one({
        'url' : short_url,
        'shorten_url' : short_url,
        'creation_date' : datetime.utcnow(),
        'expiration' : None
    })
