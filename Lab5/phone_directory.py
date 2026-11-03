contacts = {
    "Anita": {"phones": ["9876543210"], "email": "anita@mail.com", "city": "Pune"},
    "Manoj": {"phones": ["9123456780", "9988776655"], "email": "manoj@mail.com", "city": "Delhi"},
    "Zara": {"phones": ["9000011111"], "email": "zara@mail.com", "city": "Pune"},
}


def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def owner_of(phone):
    lookup = {number: name for name, record in contacts.items() for number in record["phones"]}
    return lookup.get(phone)


def reports():
    city_groups = {}
    for name, record in contacts.items():
        city_groups.setdefault(record["city"], []).append(name)
    print("Grouped by city:", {city: sorted(names) for city, names in city_groups.items()})
    print("More than one number:", sorted(name for name, record in contacts.items() if len(record["phones"]) > 1))
    print("Directory:")
    for name in sorted(contacts):
        print(name, contacts[name])


while True:
    print("\n1 Add  2 Add number  3 Update  4 Delete  5 Search  6 Reports  7 Exit")
    choice = input("Choose: ")
    if choice == "1":
        name = input("Name: ").strip()
        phone = input("Phone: ").strip()
        if name in contacts:
            print("Contact already exists.")
        elif not valid_phone(phone):
            print("Phone must be exactly 10 digits.")
        elif owner_of(phone):
            print(f"Number belongs to {owner_of(phone)}.")
        else:
            contacts[name] = {"phones": [phone], "email": input("Email: ").strip(), "city": input("City: ").strip()}
            print("Contact added.")
    elif choice == "2":
        name, phone = input("Name: ").strip(), input("Phone: ").strip()
        if name not in contacts:
            print("Contact not found.")
        elif not valid_phone(phone):
            print("Phone must be exactly 10 digits.")
        elif owner_of(phone):
            print(f"Number belongs to {owner_of(phone)}.")
        else:
            contacts[name]["phones"].append(phone)
            print("Number added.")
    elif choice == "3":
        record = contacts.get(input("Name: ").strip())
        if not record:
            print("Contact not found.")
        else:
            field = input("Update email or city: ").lower().strip()
            if field in {"email", "city"}:
                record[field] = input(f"New {field}: ").strip()
                print("Contact updated.")
            else:
                print("Invalid field.")
    elif choice == "4":
        print("Contact deleted." if contacts.pop(input("Name: ").strip(), None) else "Contact not found.")
    elif choice == "5":
        query = input("Partial name or 10-digit phone: ").strip()
        if valid_phone(query):
            print(owner_of(query) or "Number not found.")
        else:
            found = [name for name in contacts if query.lower() in name.lower()]
            print(found or "No contacts found.")
    elif choice == "6":
        reports()
    elif choice == "7":
        break
    else:
        print("Invalid choice.")
