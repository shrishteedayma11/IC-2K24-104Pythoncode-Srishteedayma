while True:
    print("\nMenu")
    print("1. Square a number")
    print("2. Check even or odd")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        number = float(input("Enter a number: "))
        print(f"Square: {number ** 2}")
    elif choice == "2":
        number = int(input("Enter an integer: "))
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
