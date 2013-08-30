from momdad import app
from flask import redirect, reverse, render_template
from models import Page


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

