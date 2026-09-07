matrix = []

for row in range(3):
    while True:
        values = input(f"Enter 3 values for row {row + 1}, separated by spaces: ").split()
        if len(values) == 3:
            matrix.append([int(value) for value in values])
            break
        print("Please enter exactly 3 integer values.")

total = 0
diagonal_total = 0
largest = matrix[0][0]
smallest = matrix[0][0]

for row in range(3):
    for column in range(3):
        value = matrix[row][column]
        total += value

        if row == column:
            diagonal_total += value
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value

print("\nMatrix:")
for row in matrix:
    for value in row:
        print(value, end="\t")
    print()

print(f"Sum of all elements: {total}")
print(f"Sum of main diagonal elements: {diagonal_total}")
print(f"Largest element: {largest}")
print(f"Smallest element: {smallest}")

print("Transpose:")
for column in range(3):
    for row in range(3):
        print(matrix[row][column], end="\t")
    print()
