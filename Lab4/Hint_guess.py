import random

target = random.randint(1, 100)
attempts = 0
maximum_attempts = 10

print("Guess the number between 1 and 100.")

while attempts < maximum_attempts:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input!")
        continue

    attempts += 1
    score = (maximum_attempts - attempts) * 10

    if guess == target:
        print(f"Correct! Your score is {score + 10}.")
        break

    parity_hint = "even" if target % 2 == 0 else "odd"
    multiple_hint = " and is a multiple of 5" if target % 5 == 0 else " and is not a multiple of 5"
    remaining = maximum_attempts - attempts
    print(f"Wrong guess! Hint: The number is {parity_hint}{multiple_hint}.")
    print(f"Attempts remaining: {remaining} | Current Score: {score}")
else:
    print(f"Game over! The number was {target}.")
