# All tests for R1 - /login go here
import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash


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

class FrontEndLoginTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        # click enter button
        self.click('input[type="submit"]')
        
        # after clicking on the browser (the line above)
        # the front-end code is activated 
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics. 
        # so we patch the backend to return a specific user instance, 
        # rather than running that program. (see @ annotations above)
        
        
        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test_frontend", "#welcome-header")
        self.assert_element("#tickets div h4")
        self.assert_text("t1 100", "#tickets div h4")
    
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_valid_email(self, *_):
        """
        2006, validates that error is thrown by improper emails
        """
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "testtesttest")
        self.type("#password", "test_Frontend0!")
        # click enter button
        self.click('input[type="submit"]')      
        
        # test for error message
        self.assert_element("#message")
        self.assert_text("Email format error", "#message")
    
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_valid_password(self, *_):
        """
        2007, tests password validation properties
        """
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "asD!")
        # click enter button
        self.click('input[type="submit"]')      
        
        # test for error message
        self.assert_element("#message")
        self.assert_text("Invalid password", "#message")

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "skdjFAXaks55")
        # click enter button
        self.click('input[type="submit"]')      
        
        # test for error message
        self.assert_element("#message")
        self.assert_text("Invalid password", "#message")

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "skdljf*-#ek")
        # click enter button
        self.click('input[type="submit"]')      
        
        # test for error message
        self.assert_element("#message")
        self.assert_text("Invalid password", "#message")

        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "OPendksielsd")
        # click enter button
        self.click('input[type="submit"]')      
        
        # test for error message
        self.assert_element("#message")
        self.assert_text("Invalid password", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_login_password_failed(self, *_):
        """ Login and verify if the tickets are correctly listed."""
        # open login page
        self.open(base_url + '/login')
        # fill wrong email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "wrong_passworD!0")
        # click enter button
        self.click('input[type="submit"]')
        # make sure it shows proper error message
        self.assert_element("#message")
        self.assert_text("login failed", "#message")