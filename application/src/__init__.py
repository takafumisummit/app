from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('src.config')
db = SQLAlchemy(app)

from src import view
