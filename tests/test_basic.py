#    import unittest
#    from test_back_end import TestBase

#
##
#    # Ensure that main page requires user login
#    def test_book_route_requires_login(self):
#        response = self.client.get('/', follow_redirects=True)
#        self.assertIn(b'Login', response.data)
#
    # Ensure that welcome page loads
#    def test_welcome_route_works_as_expected(self):
#        response = self.client.get('/Home', follow_redirects=True)
#        self.assertIn(b'Home Page!', response.data)

    # Ensure that posts show up on the main page
#    def test_posts_show_up_on_main_page(self):
#        response = self.client.post(
#            '/login',
#            data=dict(email="admin@admin.com", password="admin2016"),
#            follow_redirects=True
#        )
#        self.assertIn(b"Welcome to Shuaib's Book Web Application!", response.data)