import unittest
import app
# from mock import MagicMock
from mock import patch

class TestGetUser(unittest.TestCase):

	def test_run(self):
		get_user = app.GetUser()
		actual = get_user.run()
		self.assertEqual(actual, { "name" : "Sam" } )

class TestApp(unittest.TestCase):

	def test_run(self):
		@patch('__app__.GetUser')
		def run(self, mock):
			mock.return_value = { "firstName" : "Sam" }

		try:
			app.run()
		except:
			self.fail("run raised")
