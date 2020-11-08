# Test plan

### How did your team organize the documentations of the test cases?
 

The documentaion is split by requirement groups, as in R1, R2, R3. This makes it easy for us and the TA to identity the requirements that are met. While each test case in this table isn't necessarily equivalent to each required spec (although it can be), this format allows us to group together the test cases that meet each group of requirements. Each test case has a test case ID that is uniquely for that test, regardless of requirement group or purpose. These test cases are identified by integers from 2000 upwards. The number choice is random. Since each of us (there are 4 of us in this group), we each took a range of numbers (ie. 2000-4000) for the test cases we said we would write. The table also includes a column that contains a short description of what each test ensures, which describes the purpose of the code and what spec we'd be covering.
 


### Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.

Whenever a pull request is made to master, a github workflow is dispatched where it specifies how to run the internal automated testing. It only allows the merge to be completed if all tests are passed, and no regression is created.

The test framework Selenium is a headless browser that executes Javascript actions into the browser and asserts expected elements.

The test framework pytest will execute tests on backend functions, and perform tests on the endpoints, giving values and asserting outcomes.


### How are you going to organize different test case code files?



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
| R2                 |    7000      | Check if cookie or token exists representing login, make sure redirected (F)|
| R2                 |    7001      | If there is no cookie or token rep auth, make sure on register page     (F)| 
| R2                 |    7002      | fields exist and register form can be successfully POSTed to current at register         (F)|
| R2                 |    7003      | Make sure you cannot register with email or password fields empty       (F)|
| R2                 |    7004      | Make sure when registering password 1 and password 2 matches            (F)|
| R2                 |    7005      | Email field must match the regex that defines valid emails when registering an account (B) |
| R2                 |    7006      | Password must have minimum length of 6 when registering an account (B) |
| R2                 |    7007      | Password must have one uppercase when registering an account (B) |
| R2                 |    7008      | Password must have one lowercase when registering an account (B) |
| R2                 |    7009      | Password must have one special character when registering an account (B) |
| R2                 |    7010      | Username must be non-empty when registering an account (B) |
| R2                 |    7013      | Username must be alphanumeric when registering an account (B) |
| R2                 |    7011      | Cannot have a space at the start of username when registering an account (B) |
| R2                 |    7012      | Cannot have a space at the end of username  when registering an account (B) |
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


