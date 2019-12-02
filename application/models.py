from application import db

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	title = db.Column(db.String(100), nullable=False, unique=True)
	content = db.Column(db.String(500), nullable=False, unique=True)

	def __repr__(self):
		return ''.join([
			'User: ', self.first_name, ' ', self.last_name, '\r\n',
			'Title: ', self.title, '\r\n', self.content
			])

class Book_Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	book = db.Column(db.String(60), nullable=False, unique=True)
	author = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	rating = db.Column(db.Integer)

	def __repr__(self):
		return ''.join([
			'Book: ', self.book, '\r\n',
			'Author: ', self.author
			])

class Users(db.model):
        id = db.Column(db.Integer, primary_key=True)
        email = db.Columnn(db.String(250), nullable=False, unique=True)
        password = db.Column(db.String(500), nullable=False)

        def __repr__(self):
                return ''.join(['User ID', str(self.id), '\r\n', 'Email: ', self.email])
                
