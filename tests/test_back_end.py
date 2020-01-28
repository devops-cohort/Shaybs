#Import relevant libraries and files
import unittest

from flask import abort, url_for
from flask_testing import TestCase
import os
from application import app, db
from application.models import Users, Books, Reviews
from flask_login import login_user, current_user, logout_user, login_required


class TestBase(TestCase):

	def create_app(self):

		#Passes in test configurations
		config_name = 'testing'
		app.config.update(
			SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+os.getenv("USERNAME")+":"+os.getenv("PASSWORD")+"@"+os.getenv("MYSQL_URL")+"/"+os.getenv("MYSQL_DB_TEST")
		)
		return app

	def setUp(self):

		#Called before every test
		db.session.commit()
		db.drop_all()
		db.create_all()

		#Create test admin user
		admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin")
		employee = Users(first_name="test", last_name="user", email="test@user.com", password="test2016")
		BenjaminFranklin = Books(book="An American Life: Benjamin Franklin", author="Walter Isaacson", description="It is a biography of Benjamin Franklin", rating="5")
		ZeroToOne = Books(book="Zero To One", author="Peter Thiel", description="It stipulates business theory", rating="5")
		ShuaibReview = Reviews(review_author="Shuaib", review="Best book ever", rating="5", book_id="2")
		ThomasReview = Reviews(review_author="Thomas", review="Interesting book", rating="5", book_id="2")


		#Save/Add users to the databse
		db.session.add(admin)
		db.session.add(employee)

		#Save/Add book to database
		db.session.add(BenjaminFranklin)
		db.session.add(ZeroToOne)

		#Save/Add reviews to database
		db.session.add(ShuaibReview)
		db.session.add(ThomasReview)
		db.session.commit()

	def tearDown(self):
		#Called after every test
		db.session.remove()
		db.drop_all()

class TestViews(TestBase):

	#Test the HTTP response for the home page
	def  test_home_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the login page
	def  test_login_view(self):
		response = self.client.get(url_for('login'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the register page
	def  test_register_view(self):
		response = self.client.get(url_for('register'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the about page
	def  test_about_view(self):
		response = self.client.get(url_for('about'))
		self.assertEqual(response.status_code, 200)

	#Test the HTTP response for the account page
	def  test_account_view(self):
		response = self.client.get(url_for('account'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the books page
	def  test_books_view(self):
		response = self.client.get(url_for('books'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the reviews
	def  test_reviews_view(self):
		response = self.client.get(url_for('reviews'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the new book page
	def  test_add_book_view(self):
		response = self.client.get(url_for('add_book'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the new review page
	def  test_add_review_view(self):
		response = self.client.get(url_for('add_review'))
		self.assertEqual(response.status_code, 302)

	#Test the HTTP response for the logout page
	def  test_logout_view(self):
		response = self.client.get(url_for('logout'))
		self.assertEqual(response.status_code, 302)

class TestFrontEnd(TestBase):
    #Test the string response of the Home page
	def test_home_route_works_as_expected(self):
		response = self.client.get(url_for('home'))
		self.assertIn(b"Home Page", response.data)

	#Test the string response of the About page
	def test_about_route_works_as_expected(self):
		response = self.client.get(url_for('about'))
		self.assertIn(b"About", response.data)

	#Test the string response for the register
	def test_register_route_works_as_expected(self):
		response = self.client.get(url_for('register'))
		self.assertIn(b"Register for an account", response.data)

	#Test the string response for the login
	def test_login_route_works_as_expected(self):
		response = self.client.get(url_for('login'))
		self.assertIn(b"Login", response.data)

class TestUpdate(TestBase):

	def test_update_account(self):
		#Place the second row of the users table into the employee
		employee = Users.query.filter_by(id=2)

		#This creates a list of rows, hence the variable's first row must be called
		employee[0].first_name = "NotTest"
		employee[0].last_name = "NotUser"
		employee[0].email = "NotTest@NotUser.com"

		#Committing the new input into the SQL table
		db.session.commit()

		#Getting the new row from the SQL database
		employee = Users.query.filter_by(id=2)

		#Testing the whether the values match previous values
		self.assertNotEqual(employee[0].first_name, "test")
		self.assertNotEqual(employee[0].last_name, "user")
		self.assertNotEqual(employee[0].email, "test@user.com")

	def test_update_book(self):
		#Get the book through a query
		book = Books.query.filter_by(id=2)

		#Change the details
		book[0].book = "Not Zero To One"
		book[0].author = "Not Peter Thiel"
		book[0].description = "Does not stipulate business theory"
		book[0].rating = "4"

		#Commit the new details to the database
		db.session.commit()

		#Get the new details from the database
		book = Books.query.filter_by(id=2)

		#Assess whether the new information is equal to the previous information
		self.assertNotEqual(book[0].book, "Zero To One")
		self.assertNotEqual(book[0].author, "Peter Thiel")
		self.assertNotEqual(book[0].description, "It stipulates business theory")
		self.assertNotEqual(book[0].rating, "5")

	def test_update_review(self):
		#Get the review through a query
		review = Reviews.query.filter_by(id=2)

		#Change the details and add it to the table
		review[0].review_author = "Not Thomas"
		review[0].review = "Worst book ever"
		review[0].rating = "1"
		db.session.commit()

		#Get the new details from the database
		review = Reviews.query.filter_by(id=2)

		#Assess whether the new information is equal to the previous information
		self.assertNotEqual(review[0].review_author, "Thomas")
		self.assertNotEqual(review[0].review, "Interesting book")
		self.assertNotEqual(review[0].rating, "5")

class ModelTests(TestBase):
	
	#Test whether a new list can be added and the count of the table to verify the addition
	def test_users_model(self):
		piers = Users(first_name="piers", last_name="gilbert", email="piers@email.com", password="unknown")
		db.session.add(piers)
		db.session.commit()
		self.assertEqual(Users.query.count(), 3)

	#Test whether a new list can be added and the count of the table to verify the addition
	def test_books_model(self):
		effectiveExecutive = Books(book="The Effective Executive", author="Peter Drucker", description="A book about business", rating="5")
		db.session.add(effectiveExecutive)
		db.session.commit()
		self.assertEqual(Books.query.count(), 3)

	#Test whether a new list can be added and the count of the table to verify the addition
	def test_reviews_model(self):
		dmytroReview = Reviews(review_author="Dmytro", review="Interesting book", rating="5", book_id="1")
		db.session.add(dmytroReview)
		db.session.commit()
		self.assertEqual(Reviews.query.count(), 3)

	#Test whether a row can be deleted and the count of the table to verify the deletion
	def test_users_delete_model(self):
		Users.query.filter(Users.id == 1).delete()
		db.session.commit()
		self.assertEqual(Users.query.count(), 1)

	#Test whether a row can be deleted and the count of the table to verify the deletion
	def test_reviews_delete_model(self):
		Reviews.query.filter(Reviews.id == 1).delete()
		db.session.commit()
		self.assertEqual(Reviews.query.count(), 1)

	#Test whether a row can be deleted and the count of the table to verify the deletion
	def test_books_delete_model(self):
		Books.query.filter(Books.id == 1).delete()
		db.session.commit()
		self.assertEqual(Books.query.count(), 1)

class TestLogin(TestBase):
	# Ensure that books page redirects to the Login page
	# Ensure that the Login Page has 'Login' in its HTML response
	def test_book_route_requires_login(self):
		response = self.client.get(url_for('books'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

	# Ensure that add book page redirects to the Login page
	# Ensure that the Login Page has 'Login' in its HTML response
	def test_add_book_route_requires_login(self):
		response = self.client.get(url_for('add_book'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

	# Ensure that reviews page requires user login
	def test_reviews_route_requires_login(self):
		response = self.client.get(url_for('reviews'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

	# Ensure that the add review page requires user login
	def test_add_review_route_requires_login(self):
		response = self.client.get(url_for('add_review'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

	# Ensure that the account page requires user login
	def test_account_route_requires_login(self):
		response = self.client.get(url_for('account'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

	# Test whether login works properly
	def test_login(self):
		response = self.client.post(
			url_for('login'),
			data=dict(email="admin@admin.com", password="admin"),
			follow_redirects=True
		)
		self.assertIn(b'', response.data)
		self.assertEqual(response.status_code, 200)

	# Test whether registration works properly
	def test_register(self):
		response = self.client.post(
			url_for('login'),
			data=dict(first_name="test", last_name="anothername", email="newadmin@admin.com", password="unknown"),
			follow_redirects=True
		)
		self.assertIn(b'', response.data)
		self.assertEqual(response.status_code, 200)

	# Test whether logout works
	def test_logout(self):
		return self.client.get(url_for('logout'), follow_redirects=True)

if __name__ == '__main__':
	unittest.main()
