#can register with this one, also can use this one as a basis to sign in, there is documentation here https://www.mongodb.com/docs/manual/reference/operator/update/
import pymongo

from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://ronnee:ronnee@cluster0.csxaeir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = cluster["syllabusReadIn"]

collection = db["users"]

post = {"email": "ronnee@email.com", "password": "ronnee", "reminders": []}
collection.insert_one(post)