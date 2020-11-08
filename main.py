from flask import Flask
from flask_mongoalchemy import MongoAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET'])
def name():
    return '1'