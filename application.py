import os
from flask import Flask, url_for, render_template, request, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from models import Page

app = Flask(__name__)
print 1
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
print 2
db = SQLAlchemy(app)

print "prehome"
@app.route('/')
def home():
	return "Hello"
print "pre slug"
@app.route('/<page_slug>')
def show_page(page_slug):
	page = Page.query.filter(Page.slug == page_slug).first()
	print page
	if page is None:
		return redirect(reverse("home"))
	print "prerender"
	return render_template("test.html", page=page)
	print "post render"

if __name__ == '__main__':
	app.run()