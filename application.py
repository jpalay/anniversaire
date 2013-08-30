import os

from flask import Flask, url_for, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def home():
	return "Hello"

@app.route('/<page_slug>')
def show_slide(page_slug):
	page = Page.query.filter(Page.slug == page_slug).first()
	if page is None:
		return redirect(reverse("home"))
	return render_template("test.html", page=page)


if __name__ == '__main__':
	app.run()