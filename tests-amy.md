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

### Test case 2003 - R1.4 - The login page provides a login form which requests two fields: email and passwords
Mocking:
- none

Actions:
- open /login
- check for element `#email`
- check for element `#password`

### Test case 2004 - R1.5 - The login form can be submitted as a POST request to the current URL (/login)
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

### Test case 2005 - R1.6 - Email and password both cannot be empty
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
- enter `skdjFAXaks5&5` into elem `#password`
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
