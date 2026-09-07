"""Lab 1 (optional): a menu-driven calculator."""

while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    if choice == "5":
        print("Goodbye!")
        break
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please choose 1 to 5.")
        continue

    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    if choice == "1":
        result = first_number + second_number
    elif choice == "2":
        result = first_number - second_number
    elif choice == "3":
        result = first_number * second_number
    elif second_number == 0:
        print("Cannot divide by zero.")
        continue
    else:
        result = first_number / second_number

    print(f"Result: {result}")
