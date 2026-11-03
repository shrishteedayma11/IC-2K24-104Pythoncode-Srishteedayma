employees = {
    "E1": {"name": "Kiran", "dept": "IT", "salary": 60000},
    "E2": {"name": "Sara", "dept": "HR", "salary": 45000},
    "E3": {"name": "Dev", "dept": "IT", "salary": 75000},
    "E4": {"name": "Nina", "dept": "Finance", "salary": 52000},
    "E5": {"name": "Omar", "dept": "HR", "salary": 48000},
}


def reports():
    if not employees:
        print("No employee records.")
        return
    summary = {}
    for record in employees.values():
        entry = summary.setdefault(record["dept"], {"payroll": 0, "headcount": 0})
        entry["payroll"] += record["salary"]
        entry["headcount"] += 1
    print("Department payroll and headcount:", summary)
    for dept in summary:
        best = max((record for record in employees.values() if record["dept"] == dept), key=lambda record: record["salary"])
        print(f"Highest paid in {dept}: {best['name']} ({best['salary']})")
    print("Salary order:", [(record["name"], record["salary"]) for record in sorted(employees.values(), key=lambda record: record["salary"], reverse=True)])
    raised = {emp_id: {**record, "salary": round(record["salary"] * 1.1, 2) if record["salary"] < 50000 else record["salary"]} for emp_id, record in employees.items()}
    print("New dictionary after raise:", raised)
    department = max(summary, key=lambda dept: summary[dept]["payroll"] / summary[dept]["headcount"])
    print(f"Highest average salary: {department} ({summary[department]['payroll'] / summary[department]['headcount']:.2f})")


while True:
    print("\n1 Add  2 Update salary  3 Delete  4 Search  5 Reports  6 Exit")
    choice = input("Choose: ")
    if choice == "1":
        emp_id = input("Employee ID: ").strip()
        if emp_id in employees:
            print("Duplicate employee ID.")
            continue
        try:
            employees[emp_id] = {"name": input("Name: ").strip(), "dept": input("Department: ").strip(), "salary": float(input("Salary: "))}
            print("Employee added.")
        except ValueError:
            print("Invalid salary.")
    elif choice == "2":
        record = employees.get(input("Employee ID: ").strip())
        if not record:
            print("Employee not found.")
        else:
            try:
                record["salary"] = float(input("New salary: "))
                print("Salary updated.")
            except ValueError:
                print("Invalid salary.")
    elif choice == "3":
        print("Employee deleted." if employees.pop(input("Employee ID: ").strip(), None) else "Employee not found.")
    elif choice == "4":
        record = employees.get(input("Employee ID: ").strip())
        print(record if record else "Employee not found.")
    elif choice == "5":
        reports()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
