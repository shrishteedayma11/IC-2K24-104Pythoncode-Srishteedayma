"""Lab 1: declare values of common Python data types."""

name = "Maanyta"
age = 20
height = 5.4
is_student = True

for variable_name, value in {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student,
}.items():
    print(f"Variable: {variable_name} | Value: {value} | Type: {type(value)}")
