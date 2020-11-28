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


### Test case 6001 - R4.1 - Check that the name of the ticket contains alphanumeric characters only, and that spaces are only at the beginning or end of the name.
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "te^%&^**%st_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message



### Test case 6002 - R4.2 - Check that the length of the ticket name between 6 and 60 characters (inclusive).
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message
- enter "super_duper_unnecessarily_long_ticket_name4692387346912673498712648761984376218463" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message


### Test case 6003 - R4.3 - Check that the quantity of the ticket is between 1 and 100 (inclusive)
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 125 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message
- enter "test_ticket_name" into #name
- enter 0 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message


### Test case 6005 - R4.4 - Check that the date is given in the format YYYMMDD
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter "1" to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message


### Test case 6007 - R4.6 - Check that new tickets show up in a user's profile page
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- check that the ticket is displayed correctly in the list of tickets


### Test case 6009 - R4.7 - Check that the current date is not after the ticket date
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date - 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message


### Test case 6010 - R4.8 - Check that the price is between 10 and 100 (inclusive)
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 125 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 5 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6020 - R6.1 - Check that the name of the ticket contains alphanumeric characters only, and that spaces are only at the beginning or end of the name.
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "te^%&^**%st_ticket_name" into #name
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6001 - R6.4 - Check that ticket exists in database
Assumptions:
- ticket1 = a ticket that exists in database
- ticket2 = a ticket that doesn't exist in database 

Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name for ticket1
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name for ticket2
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6001 - R6.5 - Check that the quantity requested to buy is less than the current ticket quantity
Assumptions:
- We have 30 tickets of the requested ticket

Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 99 into #quantity
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6001 - R6.6 - Check that current balance is greater than or equal to the ticket price * quantity + 40% fees  
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) in YYYYDDMM format to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6003 - R4.2 - Check that the length of the ticket name between 6 and 60 characters (inclusive).
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter " test_ticket_name " into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message
- enter "super_duper_unnecessarily_long_ticket_name4692387346912673498712648761984376218463" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6022 - R6.3 - Check that the quantity of the ticket is between 1 and 100 (inclusive)
Mocking:
- mock backend.get_user to return a test_user instance
- mock backend.create_ticket to return True

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name" into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name" into #name
- enter 125 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message
- enter "test_ticket_name" into #name
- enter 0 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6025 - R6.4 - Check that the quantity of the ticket is between 1 and 100 (inclusive)
Mocking:
- mock backend.get_user to return a test_user instance with a balance of $75
- mock backend.get_all_tickets to return two tickets worth $50 each

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- enter "test_ticket_name1" into #name
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter "test_ticket_name2" into #name
- enter 5 into #quantity
- click element input[type="submit"]
- check that the ticket is not bought, and that the user us shown the correct error

### Test case 1001 - R7.1 - Check that logging out invalidates the current section and that protected pages can no longer be accessed
Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /
- click element #logout-button
- check that user is redirected to login page
- open /
- check that user is redirected to login page

### Test case 1010 - R8.1 - Check that non-existent URLs redirect to 404 page
Actions:
- open /nonexistent_page
- check that user is redirected to 404 page