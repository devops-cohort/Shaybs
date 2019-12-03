from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users

class LoginForm(FlaskForm):
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        password = PasswordField('Password',
                validators=[
                        DataRequired()
                ]
        )

        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')

class PostForm(FlaskForm):
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

class RegistrationForm(FlaskForm):
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
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        password = PasswordField('Password',
                validators=[
                        DataRequired(),
                ]
        )

        confirm_password = PasswordField('Confirm Password',
                validators=[
                        DataRequired(),
                        EqualTo('password')
                ]
        )
        submit = SubmitField('Sign Up')

        def validate_email(self, email):
                user = Users.query.filter_by(email=email.data).first()

                if user:
                        raise ValidationError('Email is already in use!')




                
