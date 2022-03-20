from app import db
from app.model.post import Posts
from app.model.user import Users
from app.model.source import Sources

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