from application import db

class Media(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(200))
	page = db.Column(db.Integer, db.ForeignKey('page.id'))

	def __init__(self, url, page):
		self.url = url
		self.page = page

	def __repr__(self):
		return '<Media %r>' % self.url

class Image(db.Model):
	def __repr__(self):
		return '<Image %r>' % self.url

class Video(db.Model):
	def __repr__(self):
		return '<Video %r>' % self.url

class Page(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200))
	text = db.Column(db.Text)
	slug = db.Column(db.String(100))

