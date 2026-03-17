students = []

def add_student(name, age, course):
    if not name or not course:
        print("Name and course cannot be empty.")
        return
    
    if not isinstance(age, int) or age <= 0:
        print("Invalid age.")
        return

    student = {
        "name": name.strip().title(),
        "age": age,
        "course": course.strip().title()
    }
    students.append(student)
    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("⚠️ No students found.")
        return

    print("\n📚 Student List:")
    print("-" * 40)
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    print("-" * 40)

def delete_student(index):
    if index < 1 or index > len(students):
        print("❌ Invalid student number.")
        return
    
    removed = students.pop(index - 1)
    print(f"🗑️ {removed['name']} removed successfully!")

def search_student(name):
    found = [s for s in students if name.lower() in s['name'].lower()]
    
    if not found:
        print("🔍 No matching students found.")
        return
    
    print("\n🔎 Search Results:")
    for student in found:
        print(f"Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")

def update_student(index, name=None, age=None, course=None):
    if index < 1 or index > len(students):
        print("❌ Invalid student number.")
        return

    student = students[index - 1]

    if name:
        student['name'] = name.strip().title()
    if age:
        student['age'] = age
    if course:
        student['course'] = course.strip().title()

    print("✏️ Student updated successfully!")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Update Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Invalid age input.")
                continue
            course = input("Enter course: ")
            add_student(name, age, course)

        elif choice == "2":
            view_students()

        elif choice == "3":
            try:
                index = int(input("Enter student number to delete: "))
                delete_student(index)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            name = input("Enter name to search: ")
            search_student(name)

        elif choice == "5":
            try:
                index = int(input("Enter student number to update: "))
                name = input("Enter new name (leave blank to skip): ")
                age_input = input("Enter new age (leave blank to skip): ")
                course = input("Enter new course (leave blank to skip): ")

                age = int(age_input) if age_input else None
                update_student(index, name or None, age, course or None)
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice. Try again.")

# Run the program
menu()