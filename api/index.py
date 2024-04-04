from flask import Flask, jsonify
import firebase_admin
from firebase_admin import db

credentials = firebase_admin.credentials.Certificate('/firebase.json')
default_app = firebase_admin.initialize_app(credentials, {
    'databaseURL': 'https://tori-d9dd9-default-rtdb.firebaseio.com'
})

app = Flask(__name__)

@app.route('/example/smoke')
def smoke():
    ref = db.reference('example/smoke')
    data = ref.get()
    return jsonify(data), 200

@app.route('/example/flame')
def flame():
    ref = db.reference('example/flame')
    data = ref.get()
    return jsonify(data), 200

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'