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
    def test_successful_signup(self):
        "test a new user has been created"
        response = self.apps.post('/api/v1/auth/signup', data= json.dumps(self.data1),content_type='application/json')
        result = json.loads(response.data.decode('utf-8'))      
        self.assertEqual(response.status_code, 201)

    def test_empty_email_sign_up(self):
        "test new user sign up has empty email field"
        response = self.apps.post('/api/v1/auth/signup', data = json.dumps(self.data5),content_type= 'application/json')
        self.assertEqual(response.status_code,401)
        
    def test_empty_password_sign_up(self):
        "test new user sign up has empty password field"
        response = self.apps.post('/api/v1/auth/signup', data = json.dumps(self.data6),content_type= 'application/json')
        self.assertEqual(response.status_code,401)
