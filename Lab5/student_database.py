students = {
    "101": {"name": "Asha", "marks": {"Math": 88, "Physics": 76, "Chem": 92}},
    "102": {"name": "Ravi", "marks": {"Math": 35, "Physics": 58, "Chem": 64}},
    "103": {"name": "Meena", "marks": {"Math": 72, "Physics": 81, "Chem": 69}},
}


def average(record):
    marks = record["marks"].values()
    return sum(marks) / len(marks) if marks else 0


def reports():
    if not students:
        print("No student records.")
        return
    averages = {roll: round(average(record), 2) for roll, record in students.items()}
    print("Averages:", averages)
    topper = max(students, key=lambda roll: average(students[roll]))
    print(f"Topper: {students[topper]['name']} ({averages[topper]})")
    subjects = {subject for record in students.values() for subject in record["marks"]}
    print("Highest scorer in each subject:")
    for subject in sorted(subjects):
        eligible = [record for record in students.values() if subject in record["marks"]]
        winner = max(eligible, key=lambda record: record["marks"][subject])
        print(f"{subject} -> {winner['name']} ({winner['marks'][subject]})")
    below = [(record["name"], subject, mark) for record in students.values() for subject, mark in record["marks"].items() if mark < 40]
    print("Below 40:", below or "None")
    groups = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for record in students.values():
        value = average(record)
        grade = "A" if value >= 90 else "B" if value >= 75 else "C" if value >= 60 else "D" if value >= 40 else "F"
        groups[grade].append(record["name"])
    print("Grade-wise grouping:", groups)


while True:
    print("\n1 Add  2 Update marks  3 Delete  4 Show record  5 Reports  6 Exit")
    choice = input("Choose: ")
    if choice == "1":
        roll = input("Roll number: ").strip()
        if roll in students:
            print("Duplicate roll number.")
            continue
        name = input("Name: ").strip()
        students[roll] = {"name": name, "marks": {}}
        print("Student added.")
    elif choice == "2":
        roll = input("Roll number: ").strip()
        if roll not in students:
            print("Student not found.")
            continue
        subject = input("Subject: ").strip()
        try:
            mark = float(input("Marks (0-100): "))
            if not 0 <= mark <= 100:
                raise ValueError
            students[roll]["marks"][subject] = mark
            print("Marks updated.")
        except ValueError:
            print("Marks must be between 0 and 100.")
    elif choice == "3":
        roll = input("Roll number: ").strip()
        print("Student deleted." if students.pop(roll, None) else "Student not found.")
    elif choice == "4":
        record = students.get(input("Roll number: ").strip())
        print(record if record else "Student not found.")
    elif choice == "5":
        reports()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
