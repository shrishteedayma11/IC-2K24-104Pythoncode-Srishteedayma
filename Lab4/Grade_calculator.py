marks = []

for subject in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter marks for subject {subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Invalid input!")
        except ValueError:
            print("Invalid input!")

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"

student_result = {"marks": marks, "average": average, "grade": grade}

print(f"Average: {student_result['average']:.1f}")
print(f"Grade: {student_result['grade']}")
