# Lab 4 - Interactive Python Programs

## 1. ATM Simulation

**Aim:** Simulates basic ATM operations like deposits, withdrawals, and PIN checks.

**Logic:** Uses a continuous `while` loop to show a menu, updates a local balance variable based on user input, and verifies available funds before subtracting.

**Sample:** Withdrawing `6000` from a balance of `5000` prints `Error: Insufficient funds. Transaction rejected.`

## 2. Student Grade Calculator

**Aim:** Calculates the average of 5 subjects and assigns a letter grade.

**Logic:** Collects five valid marks in a list, calculates the average using `sum()`, maps it to a grade with `if`/`elif`, and stores the result in a dictionary.

**Sample:** Marks `85, 92, 78, 60, 55` produce `Average: 74.0` and `Grade: C`. Invalid entries such as `abc` print `Invalid input!`.

## 3. Reverse Guessing Game

**Aim:** The computer guesses the user's secret number efficiently.

**Logic:** Implements binary search by tracking lower and upper bounds and guessing `(low + high) // 2` until the user confirms the guess.

**Sample:** For secret number `37`: `50` (low), `25` (high), `37` (correct).

## 4. Guessing Game with Hints

**Aim:** A number guessing game where the player gets scoring and mathematical hints.

**Logic:** Uses `random` to choose a target. A `while` loop tracks up to 10 attempts and score. The modulo operator checks even/odd status and divisibility by 5 to generate hints.

**Sample:** With target `20` and guess `15`, the program reports that the number is even and a multiple of 5, with 9 attempts and score 90 remaining.

## Files

- `Atm.py` - ATM simulation
- `Grade_calculator.py` - Grade calculator
- `Reverse_guess.py` - Reverse guessing game
- `Hint_guess.py` - Guessing game with hints
- `Main_app.py` - Launch menu for the four programs
