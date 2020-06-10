import datetime

class User:
    def __init__(self,uID,fName,lName,email,cDate=datetime.datetime.utcnow(),lLogin=datetime.datetime.utcnow()):
        self.userID = uID 
        self.firstName = fName
        self.lastName = lName
        self.email = email
        self.creationDate = cDate 
        self.lastLog = lLogin
