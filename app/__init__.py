from flask import Flask, request, jsonify
from flask_cors import CORS

from .config.db import db_connection

app = Flask(__name__)
CORS(app)

db = db_connection()
collection = db.get_collection("usuarios")

@app.route("/api/usuario/registro", methods=['POST'])
def api_registro():
    try:
        data = request.get_json()
        usuario = data.get("seudonimo")
        correo = data.get("correo")
        contrasena = data.get("contrasena")
        
        if usuario and correo and contrasena:
            collection.insert_one(
                {
                    "usuario": usuario,
                    "correo": correo,
                    "contrasena": contrasena
                }
            )
            
            return jsonify({"OK": 200})
        else:
            return jsonify({"Error": "Bad Request"}), 400
    except Exception as e:
        return jsonify({
            "Error":"Ocurrió un error al procesar la solicitud."
        }), 500

    # data = {"api":"/api/usuario/registro"}
    # return jsonify(data)

@app.route("/api/usuario/iniciar_sesion", methods=["POST"])
def api_iniciar_sesion():
    try:
        data = request.get_json()
        correo = data.get("correo")

        collection = db.get_collection("usuarios")
        result = collection.find_one({"correo": correo})
        print(result)
        if result is not None:
            return jsonify({"OK", 200})
        return jsonify({"OK", 200})
        # else:
            # return jsonify({"Error": "Bad Request"}), 400
    except Exception as e:
        return jsonify({
            "Error":e
        }), 500