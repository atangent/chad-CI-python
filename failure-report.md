 - failure report in clear table form, listing test name or number, what was being tested, the nature of the failure, what the error in the code was, and what actions were taken to fix it

| Test Number | Purpose | Failure | Error in the code | How Fixed | Failures addressed or not |
| ----------- | ------- | ------- | ----------------- | --------- | ------------------------- |
| R4.3.2      | Check if the price of the ticket is not in range [10, 100] not be accepted in the selling session | The invaild price 9 has be accepted | The range of  ticket price is [1,100] in source code | Change  the range of ticket price from [1,100] to [10,100] | Addressed                 |
| 4001 R3.3 | Check header shows `'Hi {}'.format(user.name)` | `self.assert_text("Hi test_frontend", "#welcome-header")` was failing | Header was `'Welcome {}'.format(user.name)` format | Change `index.html` code to say `Hi {user.name}` instead | Addressed
