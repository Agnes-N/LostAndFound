from .import db, login_manager
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime
from datetime import datetime
datetime.utcnow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True, index=True)


    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))

    lost = db.relationship('Lost', backref='user', lazy="dynamic")
    found = db.relationship('Found', backref='user', lazy="dynamic")
    
    @property
    def password(self):
        raise AttributeError('you cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'User{self.username}'

class Lost(db.Model):
    __tablename__ = "lost"
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255), index=True, nullable=False)
    address = db.Column(db.String(255))
    name = db.Column(db.String(255))
    location = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    description = db.Column(db.String(255))
    posted_date = db.Column(db.Date(), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    found = db.relationship('Found', backref='lost', lazy="dynamic")

    def save_lost(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_lost(cls):
        Lost.lost.clear()
    
    @classmethod
    def get_lost(cls):
        lost = Lost.query.all()
        return lost

    def __repr__(self):
        return f'Lost {self.category}'

class Found(db.Model):
    __tablename__ = "fouid = db.Column(db.Integer, primary_key = True)nd"
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(255), index=True, nullable=False)
    address = db.Column(db.String(255))
    name = db.Column(db.String(255))
    f_name = db.Column(db.String(255))
    image = db.Column(db.String())
    location = db.Column(db.String(255))
    phone = db.Column(db.Integer)
    description = db.Column(db.String(255))
    posted_date = db.Column(db.Date(), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lost_id = db.Column(db.Integer, db.ForeignKey('lost.id'))
    

    def save_found(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_found(cls):
        Found.found.clear()
    
    @classmethod
    def get_found(cls):
        found = Found.query.all()
        return found

    def __repr__(self):
        return f'Found {self.category}'
