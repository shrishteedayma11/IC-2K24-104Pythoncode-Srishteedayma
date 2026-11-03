books = {
    "B1": {"title": "Python Basics", "author": "Rao", "copies": 2, "issued_to": []},
    "B2": {"title": "Data Structures", "author": "Iyer", "copies": 1, "issued_to": []},
    "B3": {"title": "Algorithms", "author": "Rao", "copies": 1, "issued_to": []},
}


def member_books():
    result = {}
    for isbn, book in books.items():
        for member in book["issued_to"]:
            result.setdefault(member, []).append(isbn)
    return result


def reports():
    author = input("Author for search: ").strip().lower()
    print("Books by author:", {isbn: book["title"] for isbn, book in books.items() if book["author"].lower() == author})
    holding = member_books()
    print("Members holding more than one book:", {member: titles for member, titles in holding.items() if len(titles) > 1})
    print("Unavailable books:", [book["title"] for book in books.values() if book["copies"] == 0])
    print("Never issued:", [book["title"] for book in books.values() if not book["issued_to"]])


while True:
    print("\n1 Add  2 Issue  3 Return  4 Search  5 Reports  6 Exit")
    choice = input("Choose: ")
    if choice == "1":
        isbn = input("ISBN: ").strip()
        try:
            copies = int(input("Copies to add: "))
            if copies <= 0:
                raise ValueError
            if isbn in books:
                books[isbn]["copies"] += copies
            else:
                books[isbn] = {"title": input("Title: ").strip(), "author": input("Author: ").strip(), "copies": copies, "issued_to": []}
            print("Book added.")
        except ValueError:
            print("Copies must be a positive integer.")
    elif choice == "2":
        isbn, member = input("ISBN: ").strip(), input("Member ID: ").strip()
        book = books.get(isbn)
        held = member_books().get(member, [])
        if not book:
            print("Book not found.")
        elif member in book["issued_to"]:
            print("Member already holds this book.")
        elif len(held) >= 2:
            print("Member has reached the 2-book limit.")
        elif book["copies"] <= 0:
            print("No copies left.")
        else:
            book["copies"] -= 1
            book["issued_to"].append(member)
            print("Book issued.")
    elif choice == "3":
        isbn, member = input("ISBN: ").strip(), input("Member ID: ").strip()
        book = books.get(isbn)
        if not book or member not in book["issued_to"]:
            print("Member does not hold this book.")
        else:
            book["issued_to"].remove(member)
            book["copies"] += 1
            print("Book returned.")
    elif choice == "4":
        book = books.get(input("ISBN: ").strip())
        print(book if book else "Book not found.")
    elif choice == "5":
        reports()
    elif choice == "6":
        break
    else:
        print("Invalid choice.")
