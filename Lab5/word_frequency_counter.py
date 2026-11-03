paragraph = input("Enter a paragraph: ").lower()
cleaned = "".join(character if character.isalnum() or character.isspace() else " " for character in paragraph)
words = cleaned.split()

if not words:
    print("No words entered.")
else:
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print("Counts:", counts)
    try:
        limit = int(input("How many top words? "))
        if limit < 1:
            raise ValueError
    except ValueError:
        limit = 1
        print("Invalid number; showing one word.")
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    print("Top words:", [f"{word} ({count})" for word, count in ordered[:limit]])
    once = sorted(word for word, count in counts.items() if count == 1)
    print("Words appearing once:", once)
    inverted = {}
    for word, count in counts.items():
        inverted.setdefault(count, []).append(word)
    for value in inverted.values():
        value.sort()
    print("Inverted:", inverted)
    by_length = {}
    for word in counts:
        by_length.setdefault(len(word), []).append(word)
    for value in by_length.values():
        value.sort()
    print("Grouped by length:", by_length)
    search = input("Search word: ").lower().strip()
    print(f"{search}: {counts[search]}" if search in counts else "Word not found.")
