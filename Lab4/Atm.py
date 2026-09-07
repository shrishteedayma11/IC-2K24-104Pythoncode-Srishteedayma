balance = 5000.0
correct_pin = "1234"

pin = input("Enter your PIN: ")

if pin != correct_pin:
    print("Error: Incorrect PIN.")
else:
    while True:
        print("\nATM Menu")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Current balance: {balance:.2f}")
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print(f"Deposit successful. Current balance: {balance:.2f}")
            else:
                print("Error: Enter a positive amount.")
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Error: Enter a positive amount.")
            elif amount > balance:
                print("Error: Insufficient funds. Transaction rejected.")
            else:
                balance -= amount
                print(f"Withdrawal successful. Current balance: {balance:.2f}")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice!")
