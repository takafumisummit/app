from src.scraping import main, Yugihoh_Scraping, sumarization
from src import db
from sqlalchemy import Column, Integer, String, Text


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

def _insert():
    db.session.query(Yugioh_Content).delete()
    lists = main()

    for list in lists:
        c1 = Yugioh_Content(name=list['name'], body=list['sentences'])
        db.session.add(c1)
        db.session.commit()
