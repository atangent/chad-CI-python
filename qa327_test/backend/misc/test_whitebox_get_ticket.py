import pytest
import requests
import datetime

from qa327_test.conftest import base_url
import qa327.backend as bn
from qa327.models import Ticket

# Mock a sample ticket
test_ticket = Ticket(
    id=1,
    user=1,
    date=datetime.datetime.now(),
    name="Avengers 2",
    price=25,
    quantity=3
)

@pytest.mark.usefixtures('server')
def test_backend_get_ticket_T1():
    # Set up valid ticket
    bn.sell_ticket(test_ticket.name, test_ticket.quantity, test_ticket.price, test_ticket.date, test_ticket.user)

    # Test #1 (valid ticket id)
    result = bn.get_ticket(test_ticket.id)
    assert result is not None
    assert result.name == test_ticket.name

@pytest.mark.usefixtures('server')
def test_backend_get_ticket_T2():
    # Test input partition #2 (invalid ticket id)
    invalid_ticket_id = 2
    result = bn.get_ticket(invalid_ticket_id)
    assert result == None
    