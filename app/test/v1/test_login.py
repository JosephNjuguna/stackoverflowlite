import unittest
import os
import json
import pytest

from app import create_app

class UserTest(unittest.TestCase):
    def setUp(self):
        self.application = create_app
        self.apps = self.application.test_client()
        "correct email with correct password in sign up "
        self.data1 = {
            "name":"winnie", 
            "email":"test1@gmail.com",
            "password":"1234567890"
        }
        "correct email with correct password in log in "
        self.data2 = {
            "email": "test1@gmail.com",
            "password": "12345678"       
        }
        "correct email with incorrect password in log in "
        self.data3 = {
            "email": "test1@gmail.com",
            "password":"123456789"       
        }
        "incorrect email with correct password in log in "
        self.data7 = {
            "email": "joe@gmail.com",
            "password":"password"       
        }
        "empty password during log in "
        self.data4 = {
            "email": "test1@gmail.com",
            "password":""       
        }
        "empty email during log in "
        self.data8 = {
            "email": "",
            "password":"password"       
        }
        "empty email during sign up authentication "
        self.data5 = {
            "name":"winnie", 
            "email":"",
            "password":"1234567890"
        }
        "empty password during sign up authentication "
        self.data6 = {
            "name":"winnie", 
            "email":"test1@gmail.com",
            "password":""
        }
    def tearDown(self):
        pass
       
    def test_good_login(self):
        """Test a user successful login"""
        response = self.apps.post('/api/v1/auth/login', data= json.dumps(self.data2), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    def test_login_fail(self):
        "test user log in fail due to incorrect email"
        response = self.apps.post('/api/v1/auth/login',data = json.dumps(self.data7),content_type ="application/json")
        self.assertEqual(response.status_code,404)
    def test_unsuccessful_emptyemail_login(self):
        response = self.apps.post('api/v1/auth/login', data = json.dumps(self.data7), content_type='application/json')
        self.assertTrue(response.status_code,401)
    def test_unsuccessful_emptypassword_login(self):
        response = self.apps.post('api/v1/auth/login', data = json.dumps(self.data7), content_type='application/json')
        self.assertTrue(response.status_code,401)
    def test_get_all_users(self):
        "Test a user sees all users available"
        response =  self.apps.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
