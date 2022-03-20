from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(230), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    app_google_play = db.Column(db.String(120), nullable=False)
    app_apps_store = db.Column(db.String(120), nullable=False)
    keyword_ig = db.Column(db.String(120), nullable=False)
    keyword_twitter = db.Column(db.String(120), nullable=False)
    app_apps_store = db.Column(db.String(120), nullable=False)
    nama_aplikasi = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    is_active = db.Column(db.BigInteger, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)