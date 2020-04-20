from flask import Flask, render_template, jsonify, request, g, render_template_string
from flask_cors import CORS
import requests
import backend.client


app = Flask(__name__)
db = None
cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get-city/<city>')
def get_city(city):
    a = (db.select_data(f'Select * from Clientes where city="{city}"'))
    print(a)
    return jsonify(a)

@app.route('/get-code/<code>')
def get_code(code):
    a = (db.select_data(f'Select * from Clientes where code="{code}"'))
    return(jsonify(a))
