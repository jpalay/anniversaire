import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABSE_URL']
db = SQLAlchemy(app)

@app.route('/')
def home():
	return "Hello"