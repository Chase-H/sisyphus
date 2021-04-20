import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy as sa
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.hybrid import hybrid_property


from app import login, db

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=sa.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return str(self.user_id)

    def update_user(self, username=None, password=None):
        if username:
            self.username = username
        if password:
            self.set_password(password)
        db.session.commit()

    def soft_delete_user(self):
        self.deleted_at = datetime.datetime.utcnow()
        db.session.commit()

    def __repr__(self):
        return (f'<User id={self.user_id},'
                f'username={self.username},'
                f'email={self.email}>')


class HighScore(UserMixin, db.Model):
    __tablename__ = 'HighScore'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=False, nullable=False)
    distanceWalked = db.Column(db.Integer, unique=False, nullable=False)
    mountainsClimbed = db.Column(db.Integer, unique=False, nullable=False)


    def update_user_record(self, username=None, distanceWalked=None, mountainsClimbed=None):
        if username:
            self.username = username
        if distanceWalked:
            self.distanceWalked = distanceWalked
        if mountainsClimbed:
            self.mountainsClimbed = mountainsClimbed
        db.session.commit()


    def __repr__(self):
        return (f'<User name={self.username},'
                f'Distance Walked={self.distanceWalked},'
                f'Mountains Climbed={self.mountainsClimbed}>')