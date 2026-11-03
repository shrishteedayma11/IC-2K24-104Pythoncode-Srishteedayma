# Lab 5 - Dictionaries and Record Systems

## Programs

- `student_database.py` - Nested student records, marks, grades, and reports.
- `employee_database.py` - Employee records, payroll, salary reports, and non-mutating raises.
- `library_record_system.py` - Book records, issue/return rules, and library reports.
- `word_frequency_counter.py` - Paragraph cleaning, word counts, grouping, and search.
- `phone_directory.py` - Contacts with multiple phones, reverse lookup, and reports.

Each program starts with the sample data from the assignment and displays its own menu.

## Part B - Predict the Output

1. `3` - `d2` refers to the same dictionary as `d`.
2. `{'x': [1, 2]}` - `.copy()` makes a shallow copy, so the list remains shared.
3. `{'b': 1, 'c': 2}` - `0` is false and is excluded by the condition.
4. `1 5 {'a': 1, 'b': 5}` - `setdefault` returns an existing value or inserts the default.
5. `{1: 'c'} 1` - `1`, `1.0`, and `True` are equal dictionary keys.
6. A `RuntimeError: dictionary changed size during iteration` occurs.
7. `None ('b', 2)` - `pop` returns its default for a missing key, and `popitem` removes the last pair.
8. `{1: 'b'}` - the later key overwrites the earlier value for the same inverted key.

## Part C - Short Reasoning Answers

1. `d2 = d` makes a second reference to the same object. `.copy()` is shallow, while `copy.deepcopy()` copies nested objects too. A student database needs a deep copy only when a fully independent nested backup is required.
2. Keys must be hashable so their location can be calculated consistently. `(1, 2)` and `"12"` can be keys; `[1, 2]` and `{1, 2}` cannot.
3. Use `d[key]` for a key that must exist, such as a selected student's marks. Use `.get(key)` for an optional lookup, such as a search result. Use `.get(key, default)` for counting words or aggregating payroll.
4. `.update()` merges several key-value pairs at once. Assignment in a loop is better when each value needs separate calculation; `.update()` is cleaner for a prepared set of changes.
5. A new salary dictionary preserves the original data for comparison and avoids accidental side effects. In-place modification is suitable when the original records must permanently change.
6. Deleting changes the dictionary during its iteration. Iterate over `list(d)` or create a filtered new dictionary instead.
7. Loop through each book's `issued_to` list and append that ISBN to each member's list. A list is needed because one member can hold multiple books.
8. Dictionary lookup is average O(1), while searching an unsorted list is O(n). A number-to-name directory makes phone reverse lookup fast.
