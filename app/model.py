from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.String(280), unique=True, nullable=False)
    username = db.Column(db.String(55), nullable=False)
    realname = db.Column(db.String(55))
    timestamp = db.Column(db.String(), nullable=False)
    longitude = db.Column(db.Float())
    latitude = db.Column(db.Float())