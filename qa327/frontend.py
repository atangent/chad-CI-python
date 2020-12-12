from flask import render_template, request, session, redirect
from qa327 import app
from flask import url_for
import qa327.backend as bn
import re
import datetime
import decimal

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""
#####
# REGISTER METHODS
#####

@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None


    if password != password2:
        error_message = "The passwords do not match"

    elif not is_valid_email(email):
        error_message = "Email format error"

    elif not is_valid_password(password):
        error_message = "Password not strong enough"
    elif not name.replace(' ', '').isalnum() or name[0] == ' ' or name[-1] == ' ':
        error_message = "Username is not alphanumeric and cannot start or end with a space"
    else:
        user = bn.get_user(email)
        if user:
            error_message = "User exists"
        elif bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."

    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')

#####
# LOGIN METHODS
#####

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


def check_empty_fields(field):
    """
    Raises error message and renders
    login html page if field is empty
    :param field: the field in question
    """
    if not field:
        return render_template('login.html',
        message='Field is required')


def is_valid_email(email):
    """
    Returns boolean for valid email
    :param email: the email in question
    """
    INVALID_EMAIL = (len(email) < 1 or \
        not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email))
    return False if INVALID_EMAIL else True


def is_valid_password(password):
    """
    Validates password complexity 
    - min length 6
    - min one upper case
    - min one lower case
    - min one special char
    :param password: the password in question
    """
    upper = lower = special = False

    for char in password:
        if not upper and char.isalnum() and char.isupper():
            upper = True
        elif not lower and char.isalnum() and char.islower():
            lower = True
        elif not special and not char.isalnum():
            special = True
        else:
            continue

    if len(password) < 6 or not upper or \
            not lower or not special:
        return False
    return True


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Re render login page with error message 
    # if pwd field is empty or wrong format
    check_empty_fields(field=password)

    user = bn.login_user(email, password)

    if not is_valid_email(email):
        return render_template('login.html', message='Email format error')
    elif not is_valid_password(password):
        return render_template('login.html', message='Invalid password')
    elif user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        return render_template('login.html', message='login failed')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')

#####
# PROFILE METHODS
#####

def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
                
        return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    message = ""
    if ('message' in request.args):
        message = request.args.get('message')
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets, message=message)

#####
# 404 METHODS
#####

@app.errorhandler(404)
def page_not_found(error):
    """
    Returns the 404 page when accessing a url that doesn't exist
    """
    return render_template('404.html')

#####
# TICKET METHODS
#####
def is_ticket_name_valid(ticket_name):
    """
    Checks if the ticket name is valid according to the specifications.
    :param ticket_name: the name of the ticket to be tested
    :returns: True if the ticket name satisfies all requirements
    """
    return (ticket_name[0].isalnum()) and \
        (ticket_name[-1].isalnum()) and \
        (all(char.isalnum() or char.isspace() for char in ticket_name[1:-1])) and \
        (6 <= len(ticket_name) <= 60)

def is_quantity_of_tickets_valid(num_tickets):
    """
    Checks if the ticket quantity is valid according to the specifications.
    :param num_tickets: the quantity of tickets to be tested
    :returns: True if the ticket quantity satisfies all requirements
    """
    return 0 < num_tickets < 100

def does_ticket_exist(ticket_id):
    """
    Checks if the ticket id exists in the database.
    :param ticket_id: the id of the ticket to be tested
    :returns: True if the ticket id exists in the database
    """
    return bn.get_ticket(ticket_id)

def is_ticket_price_valid(ticket_price):
    """
    Checks if the ticket price is valid according to the specifications.
    :param ticket_price: the price of the ticket to be tested
    :returns: True if the ticket price satisfies all requirements
    """
    return 0 <=ticket_price <= 100

def is_ticket_date_valid(ticket_date):
    """
    Checks if the ticket date is valid according to the specifications.
    :param ticket_date: the date of the ticket to be tested
    :returns: True if the ticket date satisfies all requirements
    """
    return ticket_date > datetime.datetime.now()

def does_user_have_sufficient_balance(user_balance, ticket_price):
    """
    Checks if the user has sufficient funds to purchase the ticket, including all fees and taxes.
    :param user_balance: the balance of the user
    :param ticket_price: the price of the ticket
    :returns: True if the usre has sufficient funds to purchase the ticket
    """
    return user_balance.compare(ticket_price*decimal.Decimal("1.35")*decimal.Decimal("1.05")) != -1

@app.route('/update', methods=['POST'])
def updateticket():
    message = ""

    ticket_id = request.form['ticket_id']
    ticket_name = request.form['name']
    ticket_quantity = int(request.form['quantity'])
    ticket_price = float(request.form['price'])
    ticket_date = request.form['date']
    try:
        ticket_date = datetime.datetime.strptime(ticket_date, '%Y%m%d')
    except ValueError:
        message = "Invalid date format. Please use the format YYYMMDD, i.e. 20200421."
    user_email = request.form['user']
    user = bn.get_user(user_email)

    # check ticket exists
    if not does_ticket_exist(ticket_id):
        message = "Ticket not found."
    # check name
    if not is_ticket_name_valid(ticket_name):
        message = "Ticket name is invalid."
    # check quantity
    if not is_quantity_of_tickets_valid(ticket_quantity):
        message = "Ticket quantity must be between 0 and 100."
    # check price
    if not is_ticket_price_valid(ticket_price):
        message = "Ticket price is invalid."
    # check date
    if not is_ticket_date_valid(ticket_date):
        message = "Ticket data is invalid."

    if not message: # if message is empty, indicating no validation errors
        bn.update_ticket(ticket_id, ticket_name, ticket_quantity, ticket_price, ticket_date)
        message = "Ticket successfully updated"

    # redirect user to profile page with result message
    return redirect("/?message={}".format(message))

@app.route('/buy', methods=['POST'])
def buyticket():
    ticket_id = int(request.form['ticket_id'])
    buyer_email = request.form['user']
    buyer = bn.get_user(buyer_email)

    message = ""
    user_balance = buyer.balance
    ticket_price = bn.get_ticket(ticket_id).price

    # check for sufficient funds
    if not does_user_have_sufficient_balance(user_balance, ticket_price):
        message = "User balance does not have sufficient funds."
    
    if not message: # if message is empty, indicating no validation errors
        bn.buy_ticket(ticket_id, buyer.email)
        message = "Ticket purchased successfully."

    # redirect user to profile page with result message
    return redirect("/?message={}".format(message))

@app.route('/sell', methods=['POST'])
def sellticket():
    message = ""

    ticket_name = request.form['name']
    ticket_quantity = int(request.form['quantity'])
    ticket_price = float(request.form['price'])
    ticket_date = request.form['date']
    try:
        ticket_date = datetime.datetime.strptime(ticket_date, '%Y%m%d')
    except ValueError:
        message = "Invalid date format. Please use the format YYYMMDD, i.e. 20200421."
    user_email = request.form['user']
    user = bn.get_user(user_email)

    # check name
    if not is_ticket_name_valid(ticket_name):
        message = "Ticket name is invalid."
    # check quantity
    if not is_quantity_of_tickets_valid(ticket_quantity):
        message = "Ticket quantity must be between 0 and 100."
    # check price
    if not is_ticket_price_valid(ticket_price):
        message = "Ticket price is invalid."
    # check date
    if not is_ticket_date_valid(ticket_date):
        message = "Ticket date is invalid."

    if not message: # if message is empty, indicating no validation errors
        message = "Ticket created successfully."
        bn.sell_ticket(ticket_name, ticket_quantity, ticket_price, ticket_date, user.id)

    # redirect user to profile page with result message
    return redirect("/?message={}".format(message))

