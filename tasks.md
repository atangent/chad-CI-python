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
| R2                 |    7005      | Make sure password can only be be registered with minimum length of 6   (F)|
| R2                 |    7006      | Make sure password can only be registered with a  uppercase char        (F)|
| R2                 |    7007      | Make sure password can only be registered with a lowercase char         (F)|
| R2                 |    7008      | Make sure username cannot be registered with a space as first character (F)|
| R2                 |    7009      | Make sure username cannot be registered with a space as last  character (F)|
| R2                 |    7010      | Make sure username cannot be registered with a non alphanum character   (F)|
| R2                 |    7011      | Can register when all fields are given successfully to database and successful redirect (B)        |
| R2                 |    7012      | Make sure when registering password 1 and password 2 matches            (B)|
| R2                 |    7013      | Make sure password can only be be registered with minimum length of 6   (B)|
| R2                 |    7014      | Make sure password can only be registered with a  uppercase char        (B)|
| R2                 |    7015      | Make sure password can only be registered with a lowercase char         (B)|
| R2                 |    7016      | Make sure username cannot be registered with a space as first character (B)|
| R2                 |    7017      | Make sure username cannot be registered with a space as last  character (B)|
| R2                 |    7018      | Make sure username cannot be registered with a non alphanum character   (B)|
| R2                 |    7019      | Make sure error message is properly returned when invalid Register POST (B)|
| R2                 |    7020      | |
| R2                 |    7021      | |
 (TBD)