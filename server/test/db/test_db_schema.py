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
        "password": "123"
         }
         login_response = post_rest_payload_call(self, 'http://localhost:8080/users/login', payload=login_payload)
         self.assertEqual(login_response.get("username"), "JaneFonda")

         # assert the session is present and not just none
         self.assertIn("session", login_response)
         self.assertIsNotNone(login_response["session"])
      
     def test_token_expiration_breaker(self):
      # Log in to get a valid session token

        post_rest_call(self, 'http://localhost:8080/manage/init')

        login_payload = {
        "username": "JaneFonda",
        "password": "123"
         }
        login_response = post_rest_payload_call(self, 'http://localhost:8080/users/login', payload=login_payload)
        session_token = login_response.get("session")

        self.assertIsNotNone(session_token, "Login failed: No session token returned")

        # Wait to simulate extended session use (or skip to reuse immediately)
        # time.sleep(3600)  

        # Reuse the session token to perform an action
        headers = {"session": session_token}
        response = get_rest_call(self, 'http://localhost:8080/messages', headers=headers)

        # Assert the session token is still accepted (failure expected if expiration logic)
        self.assertEqual(response.get("status"), 200, "Session should not still be valid; no expiration logic detected")

