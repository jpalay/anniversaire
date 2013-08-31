from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os

try:
    DB_URL = os.environ['DATABASE_URL']
except KeyError:
    pass

try:
    from local_settings import *
except ImportError:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
db = SQLAlchemy(app)
