from flask import render_template, request, session, redirect
from qa327 import app
from qa327 import exceptions
from flask import url_for
import qa327.backend as bn
import re
import datetime

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
    else:
        user = bn.get_user(email)
        if user:
            error_message = "User exists"
        elif not bn.register_user(email, name, password, password2):
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
    tickets = bn.get_all_tickets()
    if ('message' in request.args):
        message = request.args['message']
    else:
        message = ""
    return render_template('index.html', user=user, tickets=tickets, message=message)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')

#####
# TICKET METHODS
#####
def is_ticket_name_valid(ticket_name):
    return True if all(char.isalnum() for char in ticket_name) and 6 <= len(ticket_name) <= 60 else False

def is_quantity_of_tickets_valid(num_tickets):
    return True if num_tickets > 0 and num_tickets <= 100 else False

def does_ticket_exist(ticket_id):
    return True if bn.get_ticket(id) is not None else False

def is_ticket_price_valid(ticket_price):
    return True if ticket_price >= 0 and ticket_price <= 100 else False

def is_ticket_date_valid(ticket_date):
    try:
        datetime.datetime.strptime(ticket_date, '%Y%m%d')
        return True
    except ValueError:
        return False

def does_user_have_sufficient_balance(user_balance, ticket_price):
    return True if user_balance >= ticket_price else False

def ticket_checks(ticket_id, ticket_name, ticket_quantity, ticket_price, ticket_date):
    # update, buy
    if not does_ticket_exist(ticket_id):
        message = "Ticket not found."
        return redirect(url_for('profile', message=message))

    # sell, update, buy
    if not is_ticket_name_alphanum(ticket_name):
        message = "Ticket name can only contain alphnumeric characters."
        return redirect(url_for('profile', message=message))

    # sell, update
    if not is_quantity_of_tickets_valid(ticket_quantity):
        message = "Ticket quantity must be between 0 and 100"
        return redirect(url_for('profile', message=message))

    # sell, update
    if not is_ticket_price_valid(ticket_price):
        message = "Ticket price is invalid"
        return redirect(url_for('profile', message=message))

    # sell, update
    if not is_ticket_name_length_ok(ticket_name):
        message = "Ticket name length is more than 60 characters."
        return redirect(url_for('profile', message=message))
    
    # sell, update
    if not is_ticket_date_valid(ticket_date):
        message = "Ticket data is invalid."
        return redirect(url_for('profile', message=message))


@app.route('/update', methods=['POST'])
def update_ticket():
    ticket_id = request.form['id']
    ticket_name = request.form['name']
    ticket_quantity = request.form['quantity']
    ticket_price = request.form['price']
    ticket_date = request.form['date']

    message = "Ticket successfully updated"

    # check ticket exists
    if not does_ticket_exist(ticket_id):
        message = "Ticket not found."
    # name checks
    if not is_ticket_name_valid(ticket_name):
        message = "Ticket name is invalid."
    # quantity
    if not is_quantity_of_tickets_valid(ticket_quantity):
        message = "Ticket quantity must be between 0 and 100."
    # price
    if not is_ticket_price_valid(ticket_price):
        message = "Ticket price is invalid."
    # date
    if not is_ticket_date_valid(ticket_date):
        message = "Ticket data is invalid."

    bn.update_ticket(ticket_id, ticket_name, ticket_quantity, ticket_price, ticket_date)

    return redirect(url_for('profile', message=message))


@app.route('/buy', methods=['POST'])
def buy_ticket():
    ticket_id = request.form['ticket_id']
    buyer_id = request.form['buyer_id']

    message = "Ticket purchased successfully."
    user_balance = bn.get_user(buyer_id).balance
    ticket_price = bn.get_ticket(ticket_id).price

    if does_user_have_sufficient_balance(user_balance, ticket_price):
        message = "User balance does not have sufficient funds."
    
    bn.buy_ticket(ticket_id, buyer_id)

    return redirect(url_for('profile', message=message))


@app.route('/sell', methods=['POST'])
def sell_ticket():
    ticket_name = request.form['name']
    ticket_quantity = request.form['quantity']
    ticket_price = request.form['price']
    ticket_date = request.form['date']

    message = "Ticket created successfully."

    # name checks
    if not is_ticket_name_valid(ticket_name):
        message = "Ticket name is invalid."
    # quantity
    if not is_quantity_of_tickets_valid(ticket_quantity):
        message = "Ticket quantity must be between 0 and 100."
    # price
    if not is_ticket_price_valid(ticket_price):
        message = "Ticket price is invalid."
    # date
    if not is_ticket_date_valid(ticket_date):
        message = "Ticket data is invalid."

    bn.sell_ticket(ticket_name, ticket_quantity, ticket_price, ticket_date)

    return redirect(url_for('profile', message=message))
