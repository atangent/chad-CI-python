### Test case 4000 - R3.1 - If the user is not logged in, redirect to login page
Mocking:
- none

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /
- validate current page is /login


### Test case 4001 - R3.2 - This page shows a header 'Hi {}'.format(user.name)
Assumptions:
- the header exists with id #welcome-header

Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- validate #welcome-header text is equal to 'Hi {}'.format(user.name)


### Test case 4002 - R3.3 - This page shows user balance.
Assumptions:
- the user balance exists with id #balance
- backend.get_user returns the user's balance

Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- validate #balance text is equal to user.balance


### Test case 4003 - R3.4 - This page shows a logout link, pointing to /logout
Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- validate element a[href="/logout"] exists


### Test case 4004 - R3.5 - This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
Assumptions:
- the ticket table exists with id #ticket-table

Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.get_tickets to return all available tickets

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- iterate through rows of #ticket-table
    - validate each row matches the row from backend.get_tickets


### Test case 4005 - R3.5 - This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
Assumptions:
- the add ticket form exists with id #add-ticket

Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.get_tickets to return all available tickets

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- iterate through fields of #add-ticket, check for name, quantity, price, expiration date


### Test case 4006 - R3.5 - This page contains a form that a user can buy new tickets. Fields: name, quantity
Assumptions:
- the add ticket form exists with id #buy-ticket

Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.get_tickets to return all available tickets

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- iterate through fields of #buy-ticket, check for name, quantity