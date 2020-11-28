# Black box testing analysis for backend.login_user

## Input partitioning

| Input # | Valid username | Correct password | Expected output |
| - | - | - | - |
| 1 | Yes | Yes | returns the corresponding User object |
| 2 | Yes | No | returns None |
| 3 | No | Yes | returns None |
| 4 | No | No | returns None |

