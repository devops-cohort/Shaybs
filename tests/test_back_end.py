import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Users, Books, Reviews
from flask_login import login_user, current_user, logout_user, login_required


class TestBase(TestCase):

	def create_app(self):

		#Passes in test configurations
		config_name = 'testing'
		app.config.update(
			SQLALCHEMY_DATABASE_URI='mysql+pymysql://'+str(getenv('USERNAME'))+':'+str(getenv('PASSWORD'))+'@35.197.196.36/bookapp_backup'
		)
		return app

	def setUp(self):

		#Called before every test
		db.session.commit()
		db.drop_all()
		db.create_all()

		#Create test admin user
		admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2016")
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

	def  test_home_view(self):
		response = self.client.get(url_for('home'))
		self.assertEqual(response.status_code, 200)

	def  test_login_view(self):
		response = self.client.get(url_for('login'))
		self.assertEqual(response.status_code, 200)

	def  test_register_view(self):
		response = self.client.get(url_for('register'))
		self.assertEqual(response.status_code, 200)

	def  test_about_view(self):
		response = self.client.get(url_for('about'))
		self.assertEqual(response.status_code, 200)

	def  test_account_view(self):
		response = self.client.get(url_for('account'))
		self.assertEqual(response.status_code, 302)

	def  test_books_view(self):
		response = self.client.get(url_for('books'))
		self.assertEqual(response.status_code, 302)

	def  test_reviews_view(self):
		response = self.client.get(url_for('reviews'))
		self.assertEqual(response.status_code, 302)

	def  test_add_book_view(self):
		response = self.client.get(url_for('add_book'))
		self.assertEqual(response.status_code, 302)

	def  test_add_review_view(self):
		response = self.client.get(url_for('add_review'))
		self.assertEqual(response.status_code, 302)

	def  test_logout_view(self):
		response = self.client.get(url_for('logout'))
		self.assertEqual(response.status_code, 302)

class TestUpdate(TestBase):

	def test_update_account(self):

		employee = Users.query.filter_by(id=2)

		employee[0].first_name = "NotTest"
		employee[0].last_name = "NotUser"
		employee[0].email = "NotTest@NotUser.com"

		db.session.commit()

		employee = Users.query.filter_by(id=2)

		self.assertNotEqual(employee[0].first_name, "test")
		self.assertNotEqual(employee[0].last_name, "user")
		self.assertNotEqual(employee[0].email, "test@user.com")

	def test_update_book(self):

		book = Books.query.filter_by(id=2)

		book[0].book = "Not Zero To One"
		book[0].author = "Not Peter Thiel"
		book[0].description = "Does not stipulate business theory"
		book[0].rating = "4"

		db.session.commit()

		book = Books.query.filter_by(id=2)

		self.assertNotEqual(book[0].book, "Zero To One")
		self.assertNotEqual(book[0].author, "Peter Thiel")
		self.assertNotEqual(book[0].description, "It stipulates business theory")
		self.assertNotEqual(book[0].rating, "5")

	def test_update_review(self):

		review = Reviews.query.filter_by(id=2)

		review[0].review_author = "Not Thomas"
		review[0].review = "Worst book ever"
		review[0].rating = "1"
		db.session.commit()

		review = Reviews.query.filter_by(id=2)

		self.assertNotEqual(review[0].review_author, "Thomas")
		self.assertNotEqual(review[0].review, "Interesting book")
		self.assertNotEqual(review[0].rating, "5")


class TestDelete(TestBase):
	def test_update_review(self):

		review = Reviews.query.filter_by(id=2)

		review[0].review_author = "Not Thomas"
		review[0].review = "Worst book ever"
		review[0].rating = "1"
		db.session.commit()

		review = Reviews.query.filter_by(id=2)

		self.assertNotEqual(review[0].review_author, "Thomas")
		self.assertNotEqual(review[0].review, "Interesting book")
		self.assertNotEqual(review[0].rating, "5")


#Test the models
# class ModelTests(TestBase):
# 	#
# 	def test_employee_model(self):
# 		self.assertEqual(Employee.query.count(), 2)

# 	def test_role_model(self):
# 		role = Role(name="CEO", description="Run the whole company")
# 		db.session.add(role)
# 		db.session.commit()
# 		self.assertEqual(Role.query.count(), 1)

# 	def test_role_model(self):
# 		role = Role(name="CEO", description="Run the whole company")
# 		db.session.add(role)
# 		db.session.commit()
# 		self.assertEqual(Role.query.count(), 1)

class TestLogin(TestBase):

    # Ensure that main page requires user login
	def test_book_route_requires_login(self):
		response = self.client.get(url_for('books'), follow_redirects=True)
		self.assertIn(b'Login', response.data)

    # Ensure that welcome page loads
	def test_home_route_works_as_expected(self):
		response = self.client.get(url_for('home'), follow_redirects=True)
		self.assertIn(b"Home Page", response.data)


	def test_login(self, admin.email, admin.password):
		return self.client.post(
			url_for('login'),
			data=dict(email=email, password=password),
			follow_redirects=True
			)

	def test_logout(self):
		return self.client.get(url_for('logout'), follow_redirects=True)

if __name__ == '__main__':
	unittest.main()
