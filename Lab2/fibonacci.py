def fibonacci_recursive(number):
    if number <= 1:
        return number
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    first, second = 0, 1
    loop_values = []
    for _ in range(terms):
        loop_values.append(first)
        first, second = second, first + second

    recursive_values = [fibonacci_recursive(index) for index in range(terms)]
    print("Loop version:", *loop_values)
    print("Recursive version:", *recursive_values)
