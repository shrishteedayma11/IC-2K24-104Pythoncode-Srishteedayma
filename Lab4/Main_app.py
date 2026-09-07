import subprocess
import sys
from pathlib import Path

programs = {
    "1": "Atm.py",
    "2": "Grade_calculator.py",
    "3": "Reverse_guess.py",
    "4": "Hint_guess.py",
}

while True:
    print("\nLab 4 Main Menu")
    print("1. ATM Simulation")
    print("2. Student Grade Calculator")
    print("3. Reverse Guessing Game")
    print("4. Guessing Game with Hints")
    print("5. Exit")
    choice = input("Choose an option: ")

    if choice == "5":
        break
    if choice in programs:
        program_path = Path(__file__).parent / programs[choice]
        subprocess.run([sys.executable, str(program_path)], check=False)
    else:
        print("Invalid choice!")
