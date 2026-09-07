import random

lower_limit = 1
upper_limit = 100
secret_number = random.randint(lower_limit, upper_limit)
attempts = 0

print(f"Guess a number between {lower_limit} and {upper_limit}.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
        break
