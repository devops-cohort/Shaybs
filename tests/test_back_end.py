import unittest

from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Users, Book_Posts

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
		#BenjaminFranklin = Book_Posts(book="An American Life: Benjamin Franklin", author="Walter Isaacson", description="It is a biography of Benjamin Franklin", rating="5")

		#Save users to the databse
		db.session.add(admin)
		db.session.add(employee)
		db.session.commit()

		#Save book to database
		#db.session.add(BenjaminFranklin)
		#db.session.commit()

	def tearDown(self):
		#Called after every test
		db.session.remove()
		db.drop_all()

class TestViews(TestBase):
	
	def  test_login_view(self):
		response = self.client.get(url_for('login'))
		self.assertEqual(response.status_code, 200)
