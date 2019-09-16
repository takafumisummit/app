from flask import render_template, request, url_for, redirect
from src import app
from sqlalchemy import Column, Integer, String, Text
from src import db


class Yugioh_Content(db.Model):
    __tablename__ = 'yugioh_contents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    body = db.Column(db.Text)


    def __init__(self, name=None, body=None):
        self.name = name
        self.body = body


    def __repr__(self):
        return '%s, %s' % (self.name, self.body)

@app.route('/', defaults={'page': 1})
@app.route("/<int:page>")
def hello(page):
    per_page = 10
    contents = Yugioh_Content.query.order_by(Yugioh_Content.id).paginate(page, per_page, error_out=False)
    return render_template("contents.html",contents=contents)

@app.route('/search', methods = ['POST', 'GET'])
def search():
   if request.method == 'POST':
      word = request.form["search"]
      search = "%{}%".format(word)
      content = Yugioh_Content.query.filter(Yugioh_Content.name.like(search)).all()
      return render_template("search.html",contents = content)

@app.route('/test/<id>', methods=['GET', 'POST'])
def google_search(id):
    word = Yugioh_Content.query.filter(Yugioh_Content.id == id).first()
    return redirect('https://www.google.com/search?q='+word.name)
