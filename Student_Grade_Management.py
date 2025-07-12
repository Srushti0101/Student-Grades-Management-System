student = {}

while True:
    print("\n--------Student Grades Management System--------")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. View Student")
    print("5. Exit")

    ch = int(input("Enter your choice : "))
    
    if ch==1:
        name = input("Enter student name : ")
        if name in student:
            print("Student already exists!")
        else:
            grade = int(input("Enter student grade : "))
            student[name] = grade
            print(f"\nAdded {name} with  a {grade}.\n")

    elif ch==2:
        update_name = input("Enter student name : ")
        if update_name in student:
            update_grade = int(input("Enter student grade : "))
            student[update_name] = update_grade
            print(f"\n{update_name} with marks are updated {update_grade}.\n")
        
        else:
            print(f"\n{name} is not found!\n")
    
    elif ch==3:
        delete_name = input("Enter student name : ")
        if delete_name in student:
            del student[delete_name]
            print(f"\n{delete_name} has been successfully deleted.\n")
        else:
            print(f"\n{delete_name} is not found!\n")
    
    elif ch==4:
        if student:
            print("\nStudent List:")
            for key,value in student.items():
                print(f"{key} : {value}")
        else:
            print("\nNo student found.\n")

    elif ch==5:
        print("\nClosing the program...\n")
        break

    else:
        print("\nInvalid choice.")