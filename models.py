import application.db as db

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
