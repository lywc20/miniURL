import datetime
from wtforms import Form, StringField, validators

class User:
    def __init__(self,uID,fName,lName,email,cDate=datetime.datetime.utcnow(),lLogin=datetime.datetime.utcnow()):
        self.userID = uID 
        self.firstName = fName
        self.lastName = lName
        self.email = email
        self.creationDate = cDate 
        self.lastLog = lLogin

class URL_Form(Form):
    url = StringField('URL',[validators.URL(require_tld=False,message="$$$ERROR: IMPROPER URL INPUT")])