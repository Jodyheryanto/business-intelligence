from app import db
from datetime import datetime
from app.model.user import Users
from app.model.source import Sources

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