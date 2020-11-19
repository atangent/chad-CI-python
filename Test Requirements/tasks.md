# Test plan

### How did your team organize the documentations of the test cases?
 

The documentaion is split by requirement groups, as in R1, R2, R3. This makes it easy for us and the TA to identity the requirements that are met. While each test case in this table isn't necessarily equivalent to each required spec (although it can be), this format allows us to group together the test cases that meet each group of requirements. Each test case has a test case ID that is uniquely for that test, regardless of requirement group or purpose. These test cases are identified by integers from 2000 upwards. The number choice is random. Since each of us (there are 4 of us in this group), we each took a range of numbers (ie. 2000-4000) for the test cases we said we would write. The table also includes a column that contains a short description of what each test ensures, which describes the purpose of the code and what spec we'd be covering.
 


### Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.

Whenever a pull request is made to master, a github workflow is dispatched where it specifies how to run the internal automated testing. It only allows the merge to be completed if all tests are passed, and no regression is created.

The test framework Selenium is a headless browser that executes Javascript actions into the browser and asserts expected elements.

The test framework pytest will execute tests on backend functions, and perform tests on the endpoints, giving values and asserting outcomes.


### How are you going to organize different test case code files?

All of our test cases will go into the qa327_test folder, then into the applicable subfolder (one of frontend, backend, or integration). We will then organize the tests into files for each requirement (R1-R8). This system will make sure tests stay organized and manageable.


# Test Cases

| Target Requirement | Test Case ID | Purpose |
|--------------------|--------------|---------|
| R1 | 2000 | Check that login page shows at when user is not logged in |
| R1 | 2001 | Check that login page has msg 'please login' |
| R1 | 2002 | Check that user profile page is shown when user is logged in |
| R1 | 2003 | Check that login form shows email and password field elements |
| R1 | 2004 | Check that login form can submit POST request to current url |
| R1 | 2005 | Check that email or password fields cannot be empty |
| R1 | 2006 | Check that input text in email field follows RFC 5322 |
| R1 | 2007 | Check that input text in password field follows complexity requirements
| R1 | 5000 | To ensure that upon logging in, any formatting errors in  the login forms are appropriately handled and the user is accordingly  prompted to fix those errors. |
| R1 | 5001 | To ensure that a user is correctly re-directed to their profile when correct  credentials have been entered on the login page. |
| R1 | 5002 | To ensure that upon logging in, if the credentials entered are incorrect, the error is appropriately handled and the user is accordingly prompted to fix the error. |

| R2 | 7000 | Check if cookie or token exists representing login, make sure redirected (F)|
| R2 | 7001 | If there is no cookie or token rep auth, make sure on register page (F)| 
| R2 | 7002 | fields exist and register form can be successfully POSTed to current at register (F)|
| R2 | 7003 | Make sure you cannot register with email or password fields empty (F)|
| R2 | 7004 | Make sure when registering password 1 and password 2 matches (F)|
| R2 | 7005 | Email field must match the regex that defines valid emails when registering an account (B) |
| R2 | 7006 | Password must have minimum length of 6 when registering an account (B) |
| R2 | 7007 | Password must have one uppercase when registering an account (B) |
| R2 | 7008 | Password must have one lowercase when registering an account (B) |
| R2 | 7009 | Password must have one special character when registering an account (B) |
| R2 | 7010 | Username must be non-empty when registering an account (B) |
| R2 | 7013 | Username must be alphanumeric when registering an account (B) |
| R2 | 7012 | Cannot have a space at the end of username  when registering an account (B) |
| R2 | 5003 | To ensure that upon an attempt to register, any formatting errors in the register forms are appropriately handled and the user is accordingly prompted to fix those errors. |
| R2 | 5004 | To ensure that upon registering, no user is allowed to sign up with an email address  which already has a user registered against in the database, and that the user is accordingly  prompted to use a different email address. |
| R2 | 5005 | To ensure that upon successful registration, the user's starting balance is set to 5000, which can be viewed from their user profile, for which they're accordingly redirected to the login page. |

| R3 | 4000 | Check that index redirects to login page if user not logged in |
| R3 | 4001 | Check that index header says Hi, user.name |
| R3 | 4002 | Check that index shows the correct user balance |
| R3 | 4003 | Check that index has a logout button |
| R3 | 4004 | Check that index lists all available tickets with correct details |
| R3 | 4005 | Check that ticket add form exists on index |
| R3 | 4006 | Check that ticket buy form exists on index |
| R3 | 5006 | To ensure that the ticket-selling form can correctly be posted to the backend (at route /sell), since details regarding the tickets are to be stored, set, and fetched from the backend. |
| R3 | 5007 | To ensure that the ticket-buying form can correctly be posted to the backend (at route /buy), since details regarding the tickets are to be stored, set, and fetched from the backend. |
| R3 | 5008 | To ensure that the ticket-update form can correctly be posted to the backend (at route /update), since details regarding the tickets are to be stored, set, and fetched from the backend. |

| R4 | 6001 | Check that the name of the ticket contains alphanumeric characters only, and that spaces are only at the beginning or end of the name. |
| R4 | 6002 | Check that the length of the ticket name between 6 and 60 characters (inclusive). |
| R4 | 6003 | Check that the quantity of the ticket is between 1 and 100 (inclusive) |
| Rj | 6004 | Check that the number of tickets is between 0 and 100 |
| R4 | 6005 | Check that the date is given in the format YYYMMDD |
| R4 | 6006 | Check that any errors result in a redirect to / and that the correct message is displayed |
| R4 | 6007 | Check that new tickets show up in a user's profile page |
| R4 | 6009 | Check that the current date is not after the ticket date |
| R4 | 6010 | Check that the price is between 10 and 100 (inclusive) |

| R5 | 6011 | Check that the name of the ticket contains alphanumeric characters only, and that spaces are only at the beginning or end of the name. |
| R5 | 6012 | Check that the length of the ticket name between 6 and 60 characters (inclusive). |
| R5 | 6013 | Check that the quantity of the ticket is between 1 and 100 (inclusive) |
| R5 | 6014 | Check that the price is between 10 and 100 (inclusive) |
| R5 | 6015 | Check that the date is given in the format YYYMMDD |
| R5 | 6016 | Check that the ticket id exists |
| R5 | 6017 | Check that any errors result in a redirect to / and that the correct message is shown |

| R5 | 6020 | Check that the name of the ticket contains alphanumeric characters only, and that spaces are only at the beginning or end of the name. |
| R5 | 6021 | Check that the length of the ticket name between 6 and 60 characters (inclusive). |
| R5 | 6022 | Check that the quantity of the ticket is between 1 and 100 (inclusive) |
| R5 | 6023 | Check that ticket exists in database
| R5 | 6024 | Check that the quantity requested to buy is less than the current ticket quantity |
| R5 | 6025 | Check that current balance is greater than or equal to the ticket price * quantity + 40% fees 
| R5 | 6026 | Check that any errors result in a redirect to / and that the correct message is shown |
