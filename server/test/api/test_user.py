# import json
# import unittest
# from unittest.mock import patch
# from server.test.test_utils import *

# class TestUser(unittest.TestCase):
#     def setUp(self):
#         """
#         initialize mock
#         """
#         self.mock_post_rest_call = patch('test.test_utils.post_rest_call').start()
#         self.mock_get_rest_call = patch('test.test_utils.get_rest_call').start()
    
#     def tearDown(self):
#         """
#         destroy mock
#         """
#         patch.stopall()
        
#     def test_login(self):
#         """
#         Log in existing account to system
#         """
#         url = "http://localhost:8080/users/register"
#         input_valid = {"username": "JaneFonda", "password": "123"}
#         input_invalid = {"username": "LoranneFonda", "password": "123"}
#         self.mock_post_rest_call.side_effect = [
#              {"error": "username or password is incorrect", "status_code": 401},       
#              {"username": input_valid["username"], "session": "2cb5b4a611c7616308e2b74c6d8085829427b7098ab8f7e8e15508435fac6d3295a70780c029c414be39feb9270a85e963d76f0efd6bcc96cf0f85e243c7ee21", "status_code": 200},
#         ]

#         self.mock_post_rest_call(url, params=input_invalid)
#         self.mock_post_rest_call(url, params=input_valid)