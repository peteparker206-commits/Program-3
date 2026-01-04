marks = {"Amber": 87, "John": 37, "Noah": 45, "Kate": 90, "Susan": 98, "Carol": 80}

choice = input("Enter the student's name: ").title()

if choice in marks:
    print(f"{choice} marks: {marks[choice]}")
else:
    print("Invalid student name entered!")
