from services.student_service import *

def menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Search Student")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")
        add_student(name, age, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        view_students()
        num = int(input("Enter number to delete: "))
        delete_student(num - 1)

    elif choice == "4":
        view_students()
        num = int(input("Enter number to update: "))
        name = input("New name: ")
        age = input("New age: ")
        course = input("New course: ")
        update_student(num - 1, name, age, course)

    elif choice == "5":
        keyword = input("Enter name to search: ")
        search_student(keyword)

    elif choice == "6":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")