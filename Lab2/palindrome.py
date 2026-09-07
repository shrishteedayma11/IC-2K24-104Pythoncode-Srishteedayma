text = input("Enter a word or phrase: ")
cleaned_text = "".join(character.lower() for character in text if character.isalnum())

if cleaned_text == cleaned_text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
