import unittest
from test.test_utils import *

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
      
     def test_token_expiration_breaker_fresh(self):
      # Log in to get a valid session token

        post_rest_call(self, 'http://localhost:8080/manage/init')

        login_payload = {
        "username": "JaneFonda",
        "password": "123"
        }

        login_response = post_rest_payload_call(self, 'http://localhost:8080/users/login', payload=login_payload)
        session_token = login_response.get("session")

        self.assertIsNotNone(session_token, "Login failed: No session token returned")
        
        post_data = {
               "username": "JaneFonda",
               "session": session_token,
               "message": "This is a test message"
            }
        post_response = post_rest_payload_call(self, 'http://localhost:8080/messages', payload=post_data)

        # Assert the session token is still accepted (failure expected if expiration logic)
        self.assertEqual(post_response.get("message"), "message created successfully", 
                         "Session should not still be valid; no expiration logic detected")
     
     def test_token_expiration_breaker_spoiled(self):
      # Log in to validate session expiration failure

        post_rest_call(self, 'http://localhost:8080/manage/init')

        login_payload = {
        "username": "JaneDoe",
        "password": "123"
        }
        
        login_response = post_rest_payload_call(self, 'http://localhost:8080/users/login', payload=login_payload)
        session_token = login_response.get("session")

        self.assertIsNotNone(session_token, "Login failed: No session token returned")

        time_travel_payload = {
            "session": session_token
        }

        time_travel_response = post_rest_payload_call(self, 'http://localhost:8080/users/goback', payload=time_travel_payload)
        self.assertEqual(time_travel_response.get("success"), "time travel successful", "something is wrong")
        
        # Reuse the session token to post a new message (which should fail due to expiration logic)
        post_data = {
               "username": "JaneDoe",
               "session": session_token,
               "message": "This is a test message"
            }
        post_response = post_rest_payload_call(self, 'http://localhost:8080/messages', expected_code=400, payload=post_data)

        # Assert the session token is still accepted (failure expected if expiration logic)
        self.assertNotEqual(post_response.get("message"), "message created successfully", 
                         "Session should not still be valid")

