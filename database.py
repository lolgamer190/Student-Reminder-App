#can register with this one, also can use this one as a basis to sign in, there is documentation here https://www.mongodb.com/docs/manual/reference/operator/update/
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://ronnee:ronnee@cluster0.csxaeir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = cluster["syllabusReadIn"]

collection = db["users"]

class LoginDetails():
    def register(self,email):
        #we can say that a code or temporary password will be sent to their email, so registration will either need a popup for the code or they'll signin with a temporary password
        collection.insert_one({"email":email, "password": "test", "name": "placeholder", "username": "placeholder", "reminders": [], "courses": []})  
     
    def checkEmail(self,email):
        if collection.find_one({"email": email}):
            return True
        else:
            return False
        

    #way to validate code on front end screen, can think about automating codes or something later, for now just a simple validate
    def validateCode(self,code):
        if code == "a1b2c3":
            return True
        
    #can use this for forgot password or changepassword
    def updatePassword(self,email, newPassword, check):
            #will need way to get email from user without prompt in the "change password screen", maybe just keeps the email or saves it as a variable somewhere to have for later after its input
            if newPassword == check:
                collection.update_one({"email": email}, {"$set":{"password":newPassword}})
                
    def updateName(self,email, name, check):
            if name == check:
                collection.update_one({"email": email}, {"$set":{"name":name}})
                
    def updateUsername(self,email, username, check):
            if username == check:
                collection.update_one({"email": email}, {"$set":{"username":username}})
   
    def updateEmail(self,email, newEmail, check):
            if newEmail == check:
                collection.update_one({"email": email}, {"$set":{"email":newEmail}})
                
    def validateAccount(self,email, password):
        if  collection.find_one({"email": email, "password": password}):
            return True
        else:
            return False
    
    def getName(self, email):
        if collection.find_one({"email": email}):
            x = collection.find_one({"email": email})
            return x["name"]
        else:
            return ""
        
    def getUsername(self, email):
        if collection.find_one({"email": email}):
            x = collection.find_one({"email": email})
            return x["username"]
        else:
            return ""
    def addCourse(self, email, course):
         collection.update_one({"email": email}, {"$set":{"courses":course}})