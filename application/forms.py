from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, FileField, IntegerField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users, Books, Reviews
from flask_login import current_user
from flask_wtf.file import FileRequired, FileAllowed

#Creates the Login form
class LoginForm(FlaskForm):
        #Add the email field and relevant data requirements
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        #Add the password field and relevant data requirements
        password = PasswordField('Password',
                validators=[
                        DataRequired()
                ]
        )

        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')
	
class Book_PostForm(FlaskForm):
        #Add the book name field and relevant data requirements
	book = StringField('Book',
		validators=[
			DataRequired(),
			Length(min=2, max=60)
		]
	)

        #Add the book author field and relevant data requirements
	author = StringField('Author(s)',
		validators=[
			DataRequired(),
			Length(min=2, max=100)
		]
	)

        #Add the book description field and relevant data requirements
	description = StringField('Description',
		validators=[
			DataRequired(),
			Length(min=2, max=250)
		]
	)

        #Add the rating field and relevant data requirements
	rating = IntegerField('Rating',
		validators=[
			NumberRange(min=0,max=5,message='Rating out of range')
		]
	)

        #Add the submit button
	submit = SubmitField('Add Book')

class ReviewForm(FlaskForm):
        #Add a query select field that ties the review to a specific book
        book = QuerySelectField(
                query_factory=lambda: Books.query.all(),
                get_label="book"
        )

        #Add the review author field and relevant data requirements
        review_author = StringField('Review Author',
                validators=[
                        DataRequired(),
                        Length(min=2, max=60)
                ]
        )

        #Add the review field and relevant data requirements
        review = StringField('Review',
                validators=[
                        DataRequired(),
                        Length(min=2, max=2000)
                ]
        )

        #Add the rating field and relevant data requirements
        rating = IntegerField('Rating',
                validators=[
                        NumberRange(min=0,max=5,message='Rating out of range')
                ]
        )

        submit = SubmitField('Add Review')

class RegistrationForm(FlaskForm):
        #Add the first name field and relevant data requirements
        first_name = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=2,max=30)
                ]
        )

        #Add the last field and relevant data requirements
        last_name = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=1,max=30)
                ]
        )

        #Add the last field and relevant data requirements
        username = StringField('Username',
                validators=[
                        DataRequired(),
                        Length(min=1,max=30)
                ]
        )

        #Add the email field and relevant data requirements
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        #Add the password field and relevant data requirements
        password = PasswordField('Password',
                validators=[
                        DataRequired(),
                ]
        )

        #Add the password field and relevant data requirements
        confirm_password = PasswordField('Confirm Password',
                validators=[
                        DataRequired(),
                        EqualTo('password')
                ]
        )

        image = FileField('Profile Picture',
                validators=[
                        FileRequired(),
                        FileAllowed(['jpg'], 'Images only')
                ]
        )
        submit = SubmitField('Sign Up')

        #Check whether the email is already in use, if it is do not allow the user to sign up
        def validate_email(self, email):
                user = Users.query.filter_by(email=email.data).first()

                if user:
                        raise ValidationError('Email is already in use!')

class UpdateAccountForm(FlaskForm):
        #Add the first name field and relevant data requirements
        first_name = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        #Add the last name field and relevant data requirements
        last_name = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        #Add the email field and relevant data requirements
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )
        submit = SubmitField('Update')

        #Check whether the email is already in use, if it is do not allow the user to sign up
        def validate_email(self, email):
                if email.data != current_user.email:
                        user = Users.query.filter_by(email=email.data).first()
                        if user:
                                raise ValidationError('Email already in use - Please choose another')

        


        
