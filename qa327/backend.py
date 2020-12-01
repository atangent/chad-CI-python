from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
import decimal

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)

    db.session.add(new_user)
    db.session.commit()
    return None

def get_ticket(ticket_id):
    """
    Get a ticket by a given id
    :param ticket_id: the id of the ticket
    :return: a ticket that has the matched id
    """
    ticket = Ticket.query.filter_by(id=ticket_id).first()
    return ticket

def update_ticket(ticket_id, name, quantity, price, date):
    """
    Update ticket info in the database
    :param ticket_id: the id of the ticket to be updated
    :param name: the name of the ticket
    :param quantity: the amount of tickets for sale
    :param price: the price of the ticket
    :param date: the expiry date of the ticket
    :return: an error message if there is any, or None if update succeeds
    """
    ticket = get_ticket(ticket_id)
    ticket.name = name
    ticket.quantity = quantity
    ticket.price = price
    ticket.date = date
    db.session.commit()

def buy_ticket(ticket_id, buyer_id):
    """
    Process ticket transaction
    :param ticket_id: the id of the ticket to be purchased
    :param buyer_id: the id of the purchasing user
    :return: an error message if there is any, or None if transaction succeeds
    """
    ticket = get_ticket(ticket_id)
    buyer = get_user(buyer_id)
    ticket.user = buyer.id
    Ticket.query.filter_by(id=ticket_id).delete()
    buyer.balance -= ticket.price*decimal.Decimal("1.35")*decimal.Decimal("1.05")
    db.session.commit()

def sell_ticket(name, quantity, price, date, user):
    """
    Create new ticket in the database
    :param ticket_id: the id of the ticket to be updated
    :param name: the name of the ticket
    :param quantity: the amount of tickets for sale
    :param price: the price of the ticket
    :param date: the expiry date of the ticket
    :param user: seller of the ticket
    :return: an error message if there is any, or None if creation succeeds
    """
    ticket = Ticket()
    ticket.name = name
    ticket.quantity = quantity
    ticket.price = price
    ticket.date = date
    ticket.user = user
    db.session.add(ticket)
    db.session.commit()

def get_all_tickets():
    """
    Get all tickets available for sale
    :return: a list of currently available tickets
    """
    tickets = Ticket.query.all()
    return tickets
