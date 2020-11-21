# All tests for R2 - register go here

import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend homepage.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!')
)

# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


class FrontEndHomePageTest(BaseCase):

    @patch('qa327.backend.register_user', return_value=test_user)
    @patch('qa327.backend.get_user', return_value=None)
    def test_register_success(self, *_):
        '''
        7002 Test if register can be successful
        '''

         #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend")
        self.type("#password", "test_Frontend0!")
        self.type("#password2", "test_Frontend0!")

        # click enter button
        self.click('input[type="submit"]')

        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Please login", "#message")

    def test_register_passwordmatch(self, *_):
        '''
        7004 make sure passwords match
        '''

        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend")
        self.type("#password", "test_Frontend0!")
        self.type("#password2", "test_Frontendend0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")

    def test_register_email(self, *_):
        '''
        7005 make sure the email is valid when registering
        '''
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "someemail")
        self.type("#name", "Test Frontend")
        self.type("#password", "test_Frontend0!")
        self.type("#password2", "test_Frontend0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Email format error", "#message")
    
    def test_register_password_minlength(self, *_):
        '''
        7006 Password must have minimum length of 6 when registering an account
        '''
        
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend")
        self.type("#password", "a1A!")
        self.type("#password2", "a1A!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")

    def test_register_password_uppercase(self, *_):
        '''
        7007 Password must have one uppercase
        '''
        
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend")
        self.type("#password", "test_frontend0!")
        self.type("#password2", "test_frontend0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")
    
    def test_register_password_lowercase(self, *_):
        '''
        7008  Password must have one lowercase when registering an account
        '''
        
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend")
        self.type("#password", "TEST_FRONTEND0!")
        self.type("#password2", "TEST_FRONTEND0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")
    
    def test_register_password_special(self, *_):
        '''
        7009  Password must have one special character
        '''
        
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend")
        self.type("#password", "test_frontend00")
        self.type("#password2", "test_frontend00")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Password not strong enough", "#message")
    
    def test_register_nonempty_username(self, *_):
        '''
        7010 Username must be non-empty when registering an account
        '''
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "$$$$$$$$")
        self.type("#password", "test_Frontend0!")
        self.type("#password2", "test_Frontend0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Username is not alphanumeric and cannot start or end with a space", "#message")
    
    def test_register_beginspace_username (self, *_):
        '''
        7011 Cannot have a space at the start of username when registering an account
        '''
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", " Test Frontend")
        self.type("#password", "test_Frontend0!")
        self.type("#password2", "test_Frontend0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Username is not alphanumeric and cannot start or end with a space", "#message")
    
    def test_register_endspace_username (self, *_):
        '''
        7012 Cannot have a space at the end of username when registering an account
        '''
        #open register page
        self.open(base_url + '/register')

        # fill in fields
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "Test Frontend ")
        self.type("#password", "test_Frontend0!")
        self.type("#password2", "test_Frontend0!")

        # click enter button
        self.click('input[type="submit"]')
        
        # Check if redirected
        self.assert_element("#message")
        self.assert_text("Username is not alphanumeric and cannot start or end with a space", "#message")