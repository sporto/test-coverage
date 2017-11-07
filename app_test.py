import unittest
import app
from mock import patch

class TestGetUser(unittest.TestCase):

	def test_get_user(self):
		actual = app.get_user()
		self.assertEqual(actual, { "name" : "Sam" } )

class TestApp(unittest.TestCase):

	def fake_get_user():
		return { "firstName" : "Sam" }

	@patch('app.get_user', side_effect=fake_get_user)
	def test_run(self, fake_get_user):
		try:
			app.run()
		except Exception as e:
			self.fail(e)
