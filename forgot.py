import pymongo

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://ronnee:ronnee@cluster0.csxaeir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = cluster["syllabusReadIn"]

collection = db["users"]

def forgotPassword():
    attempt = input("Input Code sent to your device ")

    if attempt == "1a2b3c":
        newPassword = input("New password ")
        check = input("New password again ")
        if newPassword == check:
            collection.update_one({"email": "ronnee10@yahoo.com"}, {"$set":{"password":newPassword}})
            print("Password change successful")