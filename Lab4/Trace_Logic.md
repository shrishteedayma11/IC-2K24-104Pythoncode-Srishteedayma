# Trace Logic

## ATM Withdrawal

| Balance | Withdrawal | Result |
| --- | --- | --- |
| 5000 | 6000 | Insufficient funds; transaction rejected |
| 5000 | 1200 | New balance: 3800 |

## Reverse Guessing Game

| Low | High | Guess | User response | Next range |
| --- | --- | --- | --- | --- |
| 1 | 100 | 50 | low | 1 to 49 |
| 1 | 49 | 25 | high | 26 to 49 |
| 26 | 49 | 37 | correct | Game ends |
