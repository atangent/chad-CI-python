# All tests for R5 - update go here

import pytest
from seleniumbase import BaseCase
from datetime import datetime, timedelta

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
File contains all unit tests for R5 Update

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

yesterdayobj = datetime.now() - timedelta(days=1)
yesterday = yesterdayobj.strftime('%Y%m%d')

@pytest.mark.focus
class FrontEndUpdateTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticketexists_alphanum_update(self, *_):
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
        
        # make sure ticket is on home page
        self.assert_element("#ticket-testticket")

        # update the ticket incorrectly
        self.type("#update_name", "te^%&^**%st_ticket_name")
        self.type("#update_quantity", "5")
        self.type("#update_price", "15")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_update_namelength(self, *_):
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
        
        # make sure ticket is on home page
        self.assert_element("#ticket-testticket")

        # update ticket name too short
        self.type("#update_name", "name")
        self.type("#update_quantity", "5")
        self.type("#update_price", "15")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")

        # update ticket name too long
        self.type("#update_name", "super_duper_unnecessarily_long_ticket_name4692387346912673498712648761984376218463")
        self.type("#update_quantity", "5")
        self.type("#update_price", "15")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket name is invalid.", "#message")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_update_quantity(self, *_):
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
        
        # make sure ticket is on home page
        self.assert_element("#ticket-testticket")

        # test quantity too many
        self.type("#update_name", "name")
        self.type("#update_quantity", "125")
        self.type("#update_price", "15")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket quantity must be between 0 and 100.", "#message")

        # test quantity too little
        self.type("#update_name", "name")
        self.type("#update_quantity", "0")
        self.type("#update_price", "15")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket quantity must be between 0 and 100.", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_update_price(self, *_):
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
        
        # make sure ticket is on home page
        self.assert_element("#ticket-testticket")

        # test price too little
        self.type("#update_name", "name")
        self.type("#update_quantity", "5")
        self.type("#update_price", "-1")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket price is invalid.", "#message")

        # test price too large
        self.type("#update_name", "name")
        self.type("#update_quantity", "5")
        self.type("#update_price", "125")
        self.type("#update_exp_date", nextday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket price is invalid.", "#message")
    
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_ticket_update_date(self, *_):
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
        
        # make sure ticket is on home page
        self.assert_element("#ticket-testticket")

        # test invalid date format
        self.type("#update_name", "testticket")
        self.type("#update_quantity", "5")
        self.type("#update_price", "15")
        self.type("#update_exp_date", "1")
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket data is invalid.", "#message")

        # test invalid date
        self.type("#update_name", "testticket")
        self.type("#update_quantity", "5")
        self.type("#update_price", "15")
        self.type("#update_exp_date", yesterday)
        self.click('#update_submit')
        self.assert_element("#message")
        self.assert_text("Ticket data is invalid.", "#message")