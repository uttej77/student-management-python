from students import add_student, view_students, delete_student

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")
        add_student(name, age, course)

    elif choice == "2":
        view_students()

    elif choice == "3":
        view_students()
        num = int(input("Enter student number to delete: "))
        delete_student(num - 1)

    elif choice == "4":
        break

    else:
        print("Invalid choice")