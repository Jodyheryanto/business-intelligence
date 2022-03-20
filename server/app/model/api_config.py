from app import db
from datetime import datetime

class API_Config(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    url_api = db.Column(db.String(500), nullable=False)
    param1 = db.Column(db.String(500), nullable=True)
    param2 = db.Column(db.String(500), nullable=True)
    consumer_key = db.Column(db.String(500), nullable=True)
    consumer_secret = db.Column(db.String(500), nullable=True)
    access_token = db.Column(db.String(500), nullable=True)
    access_token_secret = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return '<API_Config {}>'.format(self.url_api)
