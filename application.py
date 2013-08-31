import os
from flask import redirect, url_for, render_template
from settings import app, db
from models import *

# Views
@app.route('/')
def home():
	return "Hello"

@app.route('/<page_slug>')
def show_page(page_slug, page=None):
	page = Page.query.filter(Page.slug == page_slug).first()
	if page is None:
		return redirect(url_for("home"))
	return render_template("test.html", page=page)

if __name__ == '__main__':
	app.run()

