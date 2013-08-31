import os
from flask import Flask, redirect, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy


## configuration
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


# Views
@app.route('/')
def home():
	return "Hello"

@app.route('/add', methods=['POST'])
def add_entry():
	if not session.get('logged_in'):
		abort(401)


@app.route('/<page_slug>')
def show_page():
	page = Page.query.filter_by(slug=page_slug).first()
	if page is None:
		return redirect(url_for("home"))
	return render_template("test.html", page=page)

## Models

class Media(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(200))
	page = db.Column(db.Integer, db.ForeignKey('page.id'))

	def __init__(self, url, page):
		self.url = url
		self.page = page

	def __repr__(self):
		return '<Media %r>' % self.url

class Image(Media):
	def __repr__(self):
		return '<Image %r>' % self.url

class Video(Media):
	def __repr__(self):
		return '<Video %r>' % self.url

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200))
	text = db.Column(db.Text)
	slug = db.Column(db.String(100))

	def __init__(self, title, text, slug):
		self.title = title
		self.text = text
		self.slug = slug


if __name__ == '__main__':
	app.run()

