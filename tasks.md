# Test Cases

| Target Requirement | Test Case ID | Purpose                                                                 |
|--------------------|--------------|-------------------------------------------------------------------------|
| R1                 |     1        | Test what happens if the user hasn't logged in - should show login page |
|                    |              |                                                                         |
|                    |              |                                                                         |
|                    |              |                                                                         |
| R2                 |    7000      | Check if cookie or token exists representing login, make sure redirected (F)|
| R2                 |    7001      | If there is no cookie or token rep auth, make sure on register page     (F)| 
| R2                 |    7002      | fields exist and register form can be successfully POSTed to current at register         (F)|
| R2                 |    7003      | Make sure you cannot register with email or password fields empty       (F)|
| R2                 |    7004      | Make sure when registering password 1 and password 2 matches            (F)|
| R2                 |    7005      | Make sure an error message is returned when failing to meet a validation constraint   (F)|


# Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.

Whenever a pull request is made to master, a github workflow is dispatched where it specifies how to run the internal automated testing. It only allows the merge to be completed if all tests are passed, and no regression is created.

The test framework Selenium is a headless browser that executes Javascript actions into the browser and asserts expected elements.

The test framework pytest will execute tests on backend functions, and perform tests on the endpoints, giving values and asserting outcomes.