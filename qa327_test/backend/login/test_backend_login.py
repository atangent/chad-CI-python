import pytest
import requests

from qa327_test.conftest import base_url
import qa327.backend as bn
from qa327.models import User

# Mock a sample user
test_user = User(
    email='test@test.com',
    name='Test User',
    password='Password1!'
)

@pytest.mark.usefixtures('server')
def test_backend_login_input1():
    # Set up valid user account
    bn.register_user(test_user.email, test_user.name, test_user.password, test_user.password)

    # Test input partition #1 (valid email, correct password)
    result = bn.login_user(test_user.email, test_user.password)
    assert result is not None
    assert result.name == test_user.name

@pytest.mark.usefixtures('server')
def test_backend_login_input2():
    # Test input partition #2 (valid email, incorrect password)
    result = bn.login_user(test_user.email, "IncorrectPassword1!")
    assert result == None

@pytest.mark.usefixtures('server')
def test_backend_login_input3():
    # Test input partition #3 (invalid email, correct password)
    result = bn.login_user("incorrect@email.com", test_user.password)
    assert result == None

@pytest.mark.usefixtures('server')
def test_backend_login_input4():
    # Test input partition #4 (invalid email, incorrect password)
    result = bn.login_user("incorrect@email.com", "IncorrectPassword1!")
    assert result == None
