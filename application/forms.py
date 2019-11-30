from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class PostForm(FlaskForm):
	first_name = StringField('First Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		]
	)

	last_name = StringField('Last Name',
		validators=[
			DataRequired(),
			Length(min=2, max=30)
		]
	)

	title = StringField('Title',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		]
	)

	content = StringField('content',
		validators=[
			DataRequired(),
			Length(min=2,max=100)
		]
	)

	submit = SubmitField('Post Content')

class Book_PostForm(FlaskForm):
	book = StringField('Book',
		validators=[
			DataRequired(),
			Length(min=2, max=60)
		]
	)

	author = StringField('Author(s)',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		]
	)

	description = StringField('Description',
		validators=[
			DataRequired(),
			Length(min=2, max=250)
		]
	)

	rating = IntegerField('Rating',
		validators=[
			NumberRange(min=0,max=5,message='Rating out of range')
		]
	)

	submit = SubmitField('Post Content')
