from application import db
from flask_login import UserMixin
from datetime import datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)
    
    def __repr__(self):
            return ''.join(['User ID: ', str(self.id), '\r\n',	
                            'Email: ', self.email, '\r\n',
                           'Name: ', self.first_name, ' ', self.last_name])


class Reviews(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	review_author = db.Column(db.String(100), nullable=False)
	review = db.Column(db.String(2000), nullable=False)
	rating = db.Column(db.Integer)
	book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)

	def __repr__(self):
		return  ''.join([
			'Reviewer',  self.review_author, '\r\n',
			self.review
			])

class Books(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	book = db.Column(db.String(60), nullable=False, unique=True)
	author = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	rating = db.Column(db.Integer)
	reviews = db.relationship('Reviews', backref='book_ref', lazy=True)

	def __repr__(self):
		return ''.join([
			'Book: ', self.book, '\r\n',
			'Author: ', self.author
			])

