import unittest
from server.test.test_utils import *

class TestDBSchema(unittest.TestCase):
     def setUp(self):
        """Set up the test environment before each test."""
        post_rest_call(self, 'http://localhost:8080/manage/init')

     
     def test_user_login(self):
         post_rest_call(self, 'http://localhost:8080/manage/init')

         login_payload = {
        "username": "JaneFonda",
        "password": "12345"
         }

         login_response = post_rest_payload_call(self, 'http://localhost:8080/users/login', payload=login_payload)
         self.assertEqual({"username": "JaneFonda", "session":""})
   


