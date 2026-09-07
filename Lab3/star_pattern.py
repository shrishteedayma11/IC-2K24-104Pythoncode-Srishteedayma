number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    for row in range(1, number + 1):
        for _ in range(row):
            print("*", end="")
        print()
