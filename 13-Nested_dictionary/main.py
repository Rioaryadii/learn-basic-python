#Rio Fandia Aryadi
#241011400059
#02TPLE001

#13 - Nested Dictionary & List Practice

students = {
    "Aldi": {"math": 85, "english": 78},
    "Bella": {"math": 92, "english": 88},
    "Cika": {"math": 75, "english": 90}
}

def show_all():
    print("\n--- All Students ---")
    for name, scores in students.items():
        print(f"{name}: Math = {scores['math']}, English = {scores['english']}")

def add_student():
    name = input("Enter student name: ")
    math = int(input("Enter math score: "))
    english = int(input("Enter English score: "))
    students[name] = {"math": math, "english": english}
    print(f"{name} added.")

def update_score():
    name = input("Student to update: ")
    if name in students:
        math = int(input("New math score: "))
        english = int(input("New English score: "))
        students[name] = {"math": math, "english": english}
        print(f"{name} updated.")
    else:
        print("Student not found.")

def search_student():
    name = input("Search name: ")
    if name in students:
        s = students[name]
        print(f"{name}: Math = {s['math']}, English = {s['english']}")
    else:
        print("Not found.")

def menu():
    while True:
        print("\n1. Show All\n2. Add Student\n3. Update Score\n4. Search\n5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            show_all()
        elif choice == '2':
            add_student()
        elif choice == '3':
            update_score()
        elif choice == '4':
            search_student()
        elif choice == '5':
            break
        else:
            print("Invalid input.")

menu()