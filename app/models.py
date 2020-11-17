from app import db, login

from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	firstname = db.Column(db.String(100), nullable=False)
	lastname = db.Column(db.String(100), nullable=False)
	image_pic = db.Column(db.String(100),nullable= False, default='avatar.jpeg')
	phone_number = db.Column(db.BigInteger(), nullable=False)
	email= db.Column(db.String(50), nullable=False, unique=True)
	password_hash = db.Column(db.String(128))
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	def __repr__(self):
		return f"<User, {self.email}>"

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

class Post(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	body = db.Column(db.String(200))
	timestamp = db.Column(db.DateTime, index= True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return f"<Post, {self.timestamp}>"


@login.user_loader
def load_user(id):
	return User.query.get(int(id))