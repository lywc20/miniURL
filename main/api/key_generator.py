import secrets
from ..extensions import client
from settings import Config
from datetime import datetime

db  = client(Config.MONGO_URI).db

# Generates shortened urls
def generateKey():
    string = secrets.token_urlsafe(4)
    while not available(string):
        string = secrets.token_urlsafe(4)
    return string

# Checks if URL if shortened URL is available
def available(string):
     if db.urls.find_one({'shorten_url':string}):
         return False
     return True

# Binds the shortened URL to the original URL
def bindUrl(string,url):
    db.urls.insert_one({
        'url' : url,
        'shorten_url' : string,
        'creation_date' : datetime.utcnow(),
        'expiration' : None
    })
