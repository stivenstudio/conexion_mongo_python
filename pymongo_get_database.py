from pymongo import MongoClient

# Provide the mongodb atlas url to connect python to mongodb using pymongo
connection_string = "mongodb+srv://stiven:1234@cluster0.ezaaeig.mongodb.net/?retryWrites=true&w=majority"

def get_database():

   try:
      # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
      mongo_client = MongoClient(connection_string)
      
      # The line is printing a success message to the console indicating that the connection to MongoDB was successful.
      print("You successfully connected to MongoDB!")

      # `database = mongo_client.get_database("inventario_hoja_de_vidas")` is retrieving a reference
      database = mongo_client.get_database("base_de_datos_1")

      # `collection = database.get_collection("users")` is retrieving a reference to a collection
      collection = database.get_collection("users")

      # The `user` dictionary is creating a document that will be inserted into the MongoDB
      user = {
         "username": "user_1",
         "country": "Colombia"
      }

      # `collection.insert_one(user)` is inserting a document (in this case, the `user` dictionary)
      collection.insert_one(user)

      print("Usuario creado")
      
   except Exception as e:
      print(e)

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

   print("running")

   # Get the database
   dbname = get_database()