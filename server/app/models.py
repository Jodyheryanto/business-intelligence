from app import db
from datetime import datetime


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

class Sources(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Sources {}>'.format(self.name)

class Posts(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    username = db.Column(db.String(230), nullable=False)
    user_avatar = db.Column(db.String(255), nullable=False)
    post = db.Column(db.String(500), nullable=False)
    tanggal_post = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    users = db.relationship("Users", backref="user_id")
    source_id = db.Column(db.BigInteger, db.ForeignKey(Sources.id))
    sources = db.relationship("Sources", backref="source_id")
    link_review = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.String(1), nullable=False)
    sentiment = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.username)

class Word_Clouds(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    source_id = db.Column(db.BigInteger, db.ForeignKey(Sources.id))
    word = db.Column(db.String(50), nullable=False)
    value = db.Column(db.BigInteger, nullable=False)
    sentiment = db.Column(db.BigInteger, nullable=False)
    sample_id = db.Column(db.BigInteger, db.ForeignKey(Posts.id))
    posts = db.relationship("Posts", backref="sample_id")

    def __repr__(self):
        return '<Word_Clouds {}>'.format(self.word)

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

class Notifications(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    notif_id = db.Column(db.BigInteger, nullable=False)
    user_id = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Notifications {}>'.format(self.notif_id)

class Helps(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Helps {}>'.format(self.title)