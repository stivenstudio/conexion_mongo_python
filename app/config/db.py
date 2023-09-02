from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://root:1234@cluster0.piwxxj1.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi("1"))

def db_connection():
    try:
        print("Conectado a MongoDB")
        # database = client.get_database("hdv")
        database = client["hdv"]
        return database
    except Exception as e:
        print(e)