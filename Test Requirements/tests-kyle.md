### Test case 7000 - R2 - Check if cookie or token exists representing login, make sure redirected (F)

Assumptions:
- the home page exists
- user has been successfully authenticated in preparation for this test

Mocking:
- 

Actions:
- open /
- assert that the user is on the home page

### Test case 7001 - R2 - If there is no cookie or token rep auth, make sure on register page (F)

Assumptions:
- register page exists

Mocking:
- none

Actions:
- open /logout to invalidate existing logged-in sessions
- assert that the user is on the register page

### Test case 7002 - R2 - fields exist and register form can be successfully POSTed to current at register   (F)

Assumptions:
- register page exists
- the backend successfully manages a registration event upon a POST request

Mocking:
- creating a test_user instance 

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- enter test_user's email into element `#email`
- enter test_user's username into element `#name`
- enter test_user's password into element `#password`
- enter test_user's password2 into element `#password2`
- click element `input[type="submit"]` submit to POST to current route
- assert that the user is successfully redirected to login

### Test case 7003 - R2 - Make sure you cannot register with email or password fields empty (F)

Assumptions:
- register page exists
- the backend successfully manages a registration event upon a POST request

Mocking:
- none

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- click element `input[type="submit"]` to POST to current route POST to current route
- assert that user is still on /register and error message exists

### Test case 7004 - R2 - Make sure when registering password 1 and password 2 matches   (F)

Assumptions:
- register page exists
- the backend successfully manages a registration event upon a POST request

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- enter test_user's email into element `#email`
- enter test_user's username into element `#name`
- enter test_user's password into element `#password`
- create false second password p = "abc123ABC123"
- assure test_user's password != p, if it does, concat 'a' to p
- enter p into element `#password2`
- click element `input[type="submit"]` submit to POST to current route
- assert that the user is still on register and an error message is shown
- enter test_user's password2 into element `#password2`
- click element `input[type="submit"]` submit to POST to current route
- assert that the user is successfully redirected to login

### Test case 7005 - R2 - Make sure an error message is returned when failing to meet a validation constraint  (F)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter `a` into elem `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows
- open /login
- enter test_user's email into element `#email`
- enter `abcabcabcabcabcabcabc` into elem `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows
- open /login
- enter test_user's email into element `#email`
- enter ` bcabcabcabcabcabca` into elem `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows
- open /login
- enter test_user's email into element `#email`
- enter `bcabcabcabcabcabca ` into elem `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows
- enter test_user's email into element `#email`
- enter `bcabcabcabca$$$abca` into elem `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- compare input text in `#password` to requirements
- ensure error message shows

### Test case 7005 - R2 - Email field must match the regex that defines valid emails when registering an account

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter `myemail` into element `#email`
- enter test_user's username into element `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7006 - R2 - Password must have minimum length of 6 when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's username into element `#user`
- enter `aB12$` into element `#password`
- enter `aB12$` into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7007 - R2 - Password must have one uppercase when registering an account (B) 

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's username into element `#user`
- enter `abcdefgh12$$` into element `#password`
- enter `abcdefgh12$$` into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7008 - R2 - Password must have one lowercase when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's username into element `#user`
- enter `ABCDEFGH12$$ into element` into element `#password`
- enter `ABCDEFGH12$$ into element` into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7009 - R2 - Password must have one special character when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's username into element `#user`
- enter `abcDEF123` into element `#password`
- enter `abcDEF123` into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7010 - R2 - Username must be non-empty when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's `` into element `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7013 - R2 - Username must be alphanumeric when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- enter test_user's `$$$$$$$$$$$` into element `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7011 - R2 - Cannot have a space at the start of username when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- concatenate ` ` to the start of test_user's username then enter it into element `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows

### Test case 7012 - R2 - Cannot have a space at the end of username  when registering an account (B)

Assumptions:
- none 

Mocking:
- creating a test_user instance

Actions:
- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element `#email`
- concatenate ` ` to the end of test_user's username then enter it into element `#user`
- enter test_user's password into element `#password`
- enter test_user's password into element `#password2`
- click element `input[type="submit"]`
- ensure error message shows