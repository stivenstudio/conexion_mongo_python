from pymongo import MongoClient

# Provide the mongodb atlas url to connect python to mongodb using pymongo
connection_string = "mongodb+srv://<username>:<password>@cluster0.ezaaeig.mongodb.net/?retryWrites=true&w=majority"

def get_database():

   try:
      # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
      mongo_client = MongoClient(connection_string)
      
      # The line `print("Conectado")` is simply printing the message "Conectado" to the console. It is
      print("Conectado")

      # `database = mongo_client.get_database("inventario_hoja_de_vidas")` is retrieving a reference
      database = mongo_client.get_database("base_de_datos_1")

      # `collection = database.get_collection("users")` is retrieving a reference to a collection
      collection = database.get_collection("usuarios")

      # The `user` dictionary is creating a document that will be inserted into the MongoDB
      user = {
         "username": "Usuario 1",
         "country": "Colombia"
      }

      # `collection.insert_one(user)` is inserting a document (in this case, the `user` dictionary)
      collection.insert_one(user)

      print("Usuario creado")
      
   except Exception as e:
      print(e)

# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":

   print("Ejecutándose")

   # Get the database
   dbname = get_database()