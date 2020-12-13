# All tests for R4 - sell go here

import pytest
from seleniumbase import BaseCase
from datetime import datetime, timedelta

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file contains all unit tests for R4 Sell 

Frontend

"""

# Mock a sample ticket
test_ticket = Ticket(
    id=5,
    user=10,
    name="Test Ticket",
    price=5,
    quantity=1
)

# Mock tickets
test_tickets = [
    {
        'id': 3,
        'user': 10,
        'name': 'Test Ticket 1',
        'price': 5,
        'quantity': 2
    },
    {
        'id': 4,
        'user': 10,
        'name': 'Test Ticket 2',
        'price': 10,
        'quantity': 1
    },
]

# Mock Users
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!')
)

nextdayobj = datetime.now() + timedelta(days=1)
nextday = nextdayobj.strftime('%Y%m%d')

class FrontEndSellTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.sell_ticket', return_value=None)
    def test_ticket_works(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # create a ticket
        self.type("#sell_name", "testticket")
        self.type("#sell_quantity", "5")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket created successfully.", "#message")


    @patch('qa327.backend.get_user', return_value=test_user)
    def test_alphanum_nospaces(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # test spaces in name
        self.type("#sell_name", " test_ticket_name ")
        self.type("#sell_quantity", "5")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")

        # test alphanum name
        self.type("#sell_name", "te^%&^**%st_ticket_name")
        self.type("#sell_quantity", "5")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_name_charlength(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # test length of name too short
        self.type("#sell_name", "name")
        self.type("#sell_quantity", "5")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")
        
        # test length of name too long
        self.type("#sell_name", "super_duper_unnecessarily_long_ticket_name4692387346912673498712648761984376218463")
        self.type("#sell_quantity", "5")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_quantity(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # test quantity too many
        self.type("#sell_name", "name")
        self.type("#sell_quantity", "125")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket quantity must be between 0 and 100.", "#message")

        # test quantity too little
        self.type("#sell_name", "name")
        self.type("#sell_quantity", "0")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", nextday)
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket quantity must be between 0 and 100.", "#message")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_dateformat(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # test quantity too many
        self.type("#sell_name", "name")
        self.type("#sell_quantity", "5")
        self.type("#sell_price", "15")
        self.type("#sell_exp_date", "1")
        self.click('#sell_submit')
        self.assert_element("#message")
        self.assert_text("Ticket date is invalid.", "#message")

    








    