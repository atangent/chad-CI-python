# Test Cases

| Target Requirement | Test Case ID | Purpose                                                                 |
|--------------------|--------------|-------------------------------------------------------------------------|
| R1                 |     1        | Test what happens if the user hasn't logged in - should show login page |
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
 (TBD)