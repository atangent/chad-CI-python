# All tests for R6 - /buy go here

import pytest
import decimal
from seleniumbase import BaseCase
from datetime import datetime, timedelta

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
File contains all unit tests for R6 Buy

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
    Ticket(
        id=3,
        user=10,
        name='TestTicket1',
        price=50,
        quantity=2
    ),
    Ticket(
        id=4,
        user=10,
        name='TestTicket2',
        price=10,
        quantity=1
    )
]

# Mock Users
test_user = User(
    id=2,
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!'),
    balance=decimal.Decimal("5000")
)

broke_user = User(
    id=5,
    email='test_frontend2@test.com',
    name='test_frontend2',
    password=generate_password_hash('test_Frontend0!'),
    balance=decimal.Decimal("10")
)

nextdayobj = datetime.now() + timedelta(days=1)
nextday = nextdayobj.strftime('%Y%m%d')

yesterdayobj = datetime.now() - timedelta(days=1)
yesterday = yesterdayobj.strftime('%Y%m%d')

class FrontEndBuyTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.get_ticket', return_value=test_tickets[1])
    @patch('qa327.backend.buy_ticket', return_value=None)
    def test_ticket_buy_success(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # buy a ticket the user can't afford
        self.click('#ticket-TestTicket2-buy')
        self.click('#buy_submit')

        # assert that they failed to purchase the ticket
        self.assert_element('#message')
        self.assert_text("Ticket purchased successfully.", "#message")

    @patch('qa327.backend.get_user', return_value=broke_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.get_ticket', return_value=test_tickets[0])
    @patch('qa327.backend.buy_ticket', return_value=None)
    def test_ticket_buy_fail(self, *_):
        # log in user
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        self.click('input[type="submit"]')
        self.open(base_url)

        # buy a ticket the user can't afford
        self.click('#ticket-TestTicket1-buy')
        self.click('#buy_submit')

        # assert that they failed to purchase the ticket
        self.assert_element('#message')
        self.assert_text("User balance does not have sufficient funds.", "#message")

