import unittest
from flask import request 
from app import app
#from flask_login import FlaskLoginMixin

class AppTest(unittest.TestCase):
	LOGIN_URL = '/accounts/sign-in'
	
	def login(self,email,password):
		return self.app.post(self.LOGIN_URL, data={
			"media_email":email,
			"media_password":password
			}, follow_redirects=True)
	
	def setUp(self):
		self.app = app.test_client()
		
		
	def test_home_page_works(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code, 302)
		
	def test_about_page(self):
		response = self.app.get("/about")
		self.assertEqual(response.status_code, 200)
	"""
	def test_login(self):
		response = self.login("manqobasukzin27@gmail.com","france12")
		self.assertEqual(response.status_code, 200)
		self.assertTrue("Success" in response.data)
	"""
		
if __name__ == "__main__":
	unittest.main()