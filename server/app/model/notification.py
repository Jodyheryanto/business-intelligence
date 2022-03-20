from app import db
from datetime import datetime
from app.model.user import Users

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