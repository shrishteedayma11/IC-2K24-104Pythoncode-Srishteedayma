number = int(input("Enter a number: "))
digits = str(number)
power = len(digits)
total = sum(int(digit) ** power for digit in digits)

if total == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
