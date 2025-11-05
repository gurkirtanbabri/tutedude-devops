studentGrades = {}

def add_student(name, grade):
    studentGrades[name] = grade 

def update_grade(name, grade):
    if name in studentGrades:
        studentGrades[name] = grade
    else:
        print(f"Student {name} not found.")

def print_grades():
    for name, grade in studentGrades.items():
        print(f"{name}: {grade}")

while True:
    command = input("Enter command (add/update/print): ").strip().lower()

    if command == "add":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        add_student(name, grade)
    elif command == "update":
        name = input("Enter student name: ")
        grade = input("Enter new grade: ")
        update_grade(name, grade)
    elif command == "print":
        print_grades()