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


class HomePageTest(BaseCase):
  
  # def test_if_not_logged_in(self):
  #   self.open(base_url + '/logout')
  #   self.open(base_url)
  #   self.assert_element("#message")
  #   self.assert_text("Please login", "#message")
  
  # @patch('qa327.backend.get_user', return_value=test_user)
  # def test_header_hi_username(self, *_):
  #   self.open(base_url + '/logout')
  #   self.open(base_url + '/login')
  #   self.type("#email", "test_frontend@test.com")
  #   self.type("#password", "test_Frontend0!")
  #   self.click('input[type="submit"]')
  #   self.open(base_url)
  #   self.assert_element("#welcome-header")
  #   self.assert_text("Welcome test_frontend !", "#welcome-header")

  # @patch('qa327.backend.get_user', return_value=test_user)
  # def test_shows_user_balance(self, *_):
  #   self.open(base_url + '/logout')
  #   self.open(base_url + '/login')
  #   self.type("#email", "test_frontend@test.com")
  #   self.type("#password", "test_Frontend0!")
  #   self.click('input[type="submit"]')
  #   self.open(base_url)
  #   self.assert_text(test_user.balance, "#balance")

  # @patch('qa327.backend.get_user', return_value=test_user)
  # def test_shows_logout_link(self, *_):
  #   self.open(base_url + '/logout')
  #   self.open(base_url + '/login')
  #   self.type("#email", "test_frontend@test.com")
  #   self.type("#password", "test_Frontend0!")
  #   self.click('input[type="submit"]')
  #   self.open(base_url)
  #   self.assert_element("#logout")

  # @patch('qa327.backend.get_user', return_value=test_user)
  # @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
  # def test_list_all_tickets(self, *_):
  #   self.open(base_url + '/logout')
  #   self.open(base_url + '/login')
  #   self.type("#email", "test_frontend@test.com")
  #   self.type("#password", "test_Frontend0!")
  #   self.click('input[type="submit"]')
  #   self.open(base_url)
  #   self.assert_element("#tickets")

  # @patch('qa327.backend.get_user', return_value=test_user)
  # @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
  # def test_sell_form_fields(self, *_):
  #   self.open(base_url + '/logout')
  #   self.open(base_url + '/login')
  #   self.type("#email", "test_frontend@test.com")
  #   self.type("#password", "test_Frontend0!")
  #   self.click('input[type="submit"]')
  #   self.open(base_url)
  #   self.assert_element("#sell-ticket")
  #   self.assert_element("#sell_name")
  #   self.assert_element("#sell_quantity")
  #   self.assert_element("#sell_price")
  #   self.assert_element("#sell_exp_date")

  @patch('qa327.backend.get_user', return_value=test_user)
  @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
  def test_buy_form_fields(self, *_):
    self.open(base_url + '/logout')
    self.open(base_url + '/login')
    self.type("#email", "test_frontend@test.com")
    self.type("#password", "test_Frontend0!")
    self.click('input[type="submit"]')
    self.open(base_url)
    self.assert_element("#buy_name")
    self.assert_element("#buy_quantity")
