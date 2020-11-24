### Test case 2000 - R1.1 - If the user hasn't logged in, show the login page
Assumptions:
- the login page exists

Mocking:
- none  

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login

### Test case 2001 - R1.2 - the login page has a message that by default says 'please login'
Mocking:
- none

Actions:
- open /logout to invalidate existing logged-in sessions
- open /login
- `self.assert_exact_text` for "please login" text

### Test case 2002 - R1.3 - If the user has logged in, redirect to the user profile page
Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /login again
- validate that current page contains `#welcome-header` element

### Test case 2003 - R1.4 - The login page provides a login form which requests two fields: email and passwords (OBSOLETE))
Mocking:
- none

Actions:
- open /login
- check for element `#email`
- check for element `#password`

### Test case 2004 - R1.5 - The login form can be submitted as a POST request to the current URL (/login) (OBSOLETE)
Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- open /login again
- send post request to /login

### Test case 2005 - R1.6 - Email and password both cannot be empty (OBSOLETE)
#note: flawed because HTML blocks submission of empty fields so it won't let you press submit, that requirement only concerns backend testing
Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter nothing into element `#email`
- enter test_user's password into element `#password`
- click element `input[type="submit"]`
- make sure proper error message shows that email can't be empty
- open /login
- enter test_user's email into element `#email`
- enter nothing into element `#password`
- click element `input[type="submit"]`
- make sure error message shows that password can't be empty
- open /login
- click element `input[type="submit"]`
- make sure error message shows that fields can't be empty

### Test case 2006 - R1.7 - Email has to follow addr-spec defined in RFC 5322

Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter `testuseremail` into element `#email`
- enter test_user's pwd into elem `#password`
- click element `input[type="submit"]`
- ensure input text in element `#email` matches RFC 5322 specs
- ensure message shows that email must be valid format

### Test case 2007 - R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character
Mocking:
- mock backend.get_user to return a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter `asD!` into elem `#password`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows that pwd must meet complexity req
- open /login
- enter test_user's email into element `#email`
- enter `skdjFAXaks55` into elem `#password`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows that pwd must meet complexity req
- open /login
- enter test_user's email into element `#email`
- enter `skdljf*-#ek` into elem `#password`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows that pwd must meet complexity req
- open /login
- enter test_user's email into element `#email`
- enter `OPendksielsd` into elem `#password`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows that pwd must meet complexity req

### Test case 6001 - R5.1 - Check that the name of the ticket contains alphanumeric characters only, and that spaces are only at the beginning or end of the name.
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

### Test case 6001 - R5.2 - Check that the length of the ticket name between 6 and 60 characters (inclusive).
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
- enter " name " into #name
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6001 - R5.3 - Check that the quantity of the ticket is between 1 and 100 (inclusive)
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
- enter 1000 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6001 - R5.4 - Check that the price is between 10 and 100 (inclusive)
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
- enter 101 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message

### Test case 6001 - R5.5 - Check that the date is given in the format YYYMMDD 
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

### Test case 6001 - R5.6 - Check that the ticket id exists
Assumptions:
- ticket1 = ticket id that exists in the database
- ticket2 = ticket id that doesn't exist in the database

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
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is added, and that the user is redirected to /
- enter " test_ticket_name " into #name for ticket2
- enter 5 into #quantity
- enter 15 into #price
- enter (today's date + 1 day) to #date
- click element input[type="submit"]
- check that the ticket is not added, and that the user is redirected to / with the correct message
