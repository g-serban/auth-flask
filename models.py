from . import db


class User(db.Model):
    id = db.Colum(db.Integer, primary_key=True)  # primary keys are required by sqlalchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

