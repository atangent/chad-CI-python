# Test Cases

| Target Requirement | Test Case ID | Purpose                                                                 |
|--------------------|--------------|-------------------------------------------------------------------------|
| R1 | 2000 | Check that login page shows at when user is not logged in |
| R1 | 2001 | Check that login page has msg 'please login' |
| R1 | 2002 | Check that user profile page is shown when user is logged in |
| R1 | 2003 | Check that login form shows email and password field elements |
| R1 | 2004 | Check that login form can submit POST request to current url |
| R1 | 2005 | Check that email or password fields cannot be empty |
| R1 | 2006 | Check that input text in email field follows RFC 5322 |
| R1 | 2007 | Check that input text in password field follows complexity requirements
| R1         | 5000        	| To ensure that upon logging in, any formatting errors in  the login forms are appropriately handled and the user is accordingly  prompted to fix those errors.                                                                  	|
| R1         | 5001       	| To ensure that a user is correctly re-directed to their profile when correct  credentials have been entered on the login page.                                                                                                  	|
| R1         | 5002         | To ensure that upon logging in, if the credentials entered are incorrect, the error is appropriately handled and the user is accordingly prompted to fix the error. |
|                    |              |                                                                         |
|                    |              |                                                                         |
|                    |              | **7000 to 7014 are Client Side Tests**                                      |
| R2                 |    7000      | Check if cookie or token exists representing login, make sure redirected|
| R2                 |    7001      | If there is no cookie or token rep auth, make sure on register page     | 
| R2                 |    7002      | fields "email", "username", "password", "password2" exist on register   |
| R2                 |    7003      | register form can be successfully POSTed to current at register         |
| R2                 |    7004      | Make sure you cannot register with email or password fields empty       | (TBD)
| R2                 |    7005      | Make sure when registering password 1 and password 2 matches            | (TBD)
| R2                 |    7006      | Make sure password can only be be registered with minimum length of 6   | (TBD)
| R2                 |    7007      | Make sure password can only be registered with a  uppercase char        | (TBD)
| R2                 |    7008      | Make sure password can only be registered with a lowercase char         | (TBD)
| R2                 |    7009      | Make sure username cannot be registered with a space as first character | (TBD)
| R2                 |    7010      | Make sure username cannot be registered with a space as last  character | (TBD)
| R2                 |    7011      | Make sure username cannot be registered with a non alphanum character   | (TBD)
| R2                 |    7012      | For format errors, make sure it redirects to login and correct msg shown|
| R2                 |    7013      | If email exists, make sure appropriate message is shown                 |
| R2                 |    7014      | Make sure login sequence is successful (new acc & redirect)             |
| R2                 |    7015      | |
| R2                 |    7016      | |
| R2                 |    7017      | |
| R2                 |    7018      | |
| R2                 |    7019      | |
| R2                 |    7020      | |
| R2                 |    7021      | |
| R2                 |    7022      | |
| R2                 |    7023      | |
| R2                 |    7024      | |
| R2                 |    7025      | |
| R2         | 5003         | To ensure that upon an attempt to register, any formatting errors in the register forms are appropriately handled and the user is accordingly prompted to fix those errors.                                                     	|
| R2         | 5004         | To ensure that upon registering, no user is allowed to sign up with an email address  which already has a user registered against in the database, and that the user is accordingly  prompted to use a different email address. 	|
| R2         | 5005         | To ensure that upon successful registration, the user's starting balance is set to 5000, which can be viewed from their user profile, for which they're accordingly redirected to the login page.                               	|
| R3                 | 4000 | Check that index redirects to login page if user not logged in |
| R3                 | 4001 | Check that index header says Hi, user.name |
| R3                 | 4002 | Check that index shows the correct user balance |
| R3                 | 4003 | Check that index has a logout button |
| R3                 | 4004 | Check that index lists all available tickets with correct details |
| R3                 | 4005 | Check that ticket add form exists on index |
| R3                 | 4006 | Check that ticket buy form exists on index |
| R3         | 5006         | To ensure that the ticket-selling form can correctly be posted to the backend (at route /sell), since details regarding the tickets are to be stored, set, and fetched from the backend.                                        	|
| R3         | 5007         | To ensure that the ticket-buying form can correctly be posted to the backend (at route /buy), since details regarding the tickets are to be stored, set, and fetched from the backend.                                          	|
| R3         | 5008         | To ensure that the ticket-update form can correctly be posted to the backend (at route /update), since details regarding the tickets are to be stored, set, and fetched from the backend.                  						|
 (TBD)
