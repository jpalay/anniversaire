import os

from flask import Flask, url_for, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def home():
	return "Hello"

@app.route('/<int:slide_id>')
def show_slide(slide_id=None):
	if not slide_id:
		return url_for("home")
	return redirect(url_for("home"))

if __name__ == '__main__':
	app.run()