from flask import Flask, render_template, jsonify, request, g, render_template_string
from flask_cors import CORS
import requests
import backend.client


app = Flask(__name__)
# app.templates_auto_reload(True)
db = None
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get-data')
def get_data():
    a = (db.select_data(f'Select * from Clientes'))
    return jsonify(a)

@app.route('/delete-data/<code>')
def delete_data(code):
    a = (db.select_data(f'DELETE from Clientes where code="{code}"'))
    print("Eliminando dato")
    return jsonify("Dato eliminado correctamente de la base de datos")

@app.route('/update-data', methods=['POST'])
def update_data():
    a = request.json
    db.update_data(f'UPDATE Clientes SET name = "{a["name"]}", city = "{a["city"]}", debt = "{a["debt"]}" WHERE code = "{a["actualCode"]}"')
    print("exitoso")
    return("a")

@app.route('/create-data', methods=['POST'])
def create_data():
    a = request.json
    data = [f'"{a["code"]}", "{a["name"]}", "{a["city"]}", "{a["debt"]}"']
    print(data)
    db.insert_data(data, 'Clientes')
    return("Se inserto correctamente el dato")