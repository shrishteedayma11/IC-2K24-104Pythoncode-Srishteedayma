low = 1
high = 100

print("Think of a number between 1 and 100.")
print("Reply with low, high, or correct.")

while low <= high:
    guess = (low + high) // 2
    response = input(f"Is your number {guess}? ").strip().lower()

    if response == "correct":
        print(f"I guessed your number: {guess}")
        break
    if response == "low":
        high = guess - 1
    elif response == "high":
        low = guess + 1
    else:
        print("Please reply with low, high, or correct.")
else:
    print("Your answers were inconsistent.")
