# Solution
import re

employees = {}

def is_valid_name(name):
    return bool(re.match("[A-Za-z ]", name))

def is_valid_age(age):
    return age.isdigit() and int(age) > 0

def is_valid_department(department):
    return bool(department.strip())

def generate_emp_id():
    return f"E{len(employees) + 101}"

def add_emp():
    print("Enter Employee Details:")
    
    while True:
        name = input("Enter Name: ")
        if is_valid_name(name):
            break
        else:
            print("Invalid name! Please enter a valid name .")
    
    while True:
        age = input("Enter Age: ")
        if is_valid_age(age):
            break
        else:
            print("Invalid age! Please enter a positive integer for age.")
    
    while True:
        department = input("Enter Department: ")
        if is_valid_department(department):
            break
        else:
            print("Invalid department!")
    
    emp_id = generate_emp_id()

    employees[emp_id] = {
        "name": name,
        "age": int(age),
        "department": department
    }
    print(f"Employee {emp_id} added successfully!")

def remove_emp():
    emp_id = input("Enter Employee ID to remove: ")
    
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee {emp_id} removed successfully.")
    else:
        print("Employee ID not found.")

def update_emp():
    emp_id = input("Enter Employee ID to update: ")
    
    if emp_id in employees:
        print("Select the field to update:")
        print("1. Name")
        print("2. Age")
        print("3. Department")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            while True:
                name = input("Enter new Name (only alphabets and spaces): ")
                if is_valid_name(name):
                    employees[emp_id]["name"] = name
                    print("Name updated successfully.")
                    break
                else:
                    print("Invalid name! Please enter a valid name with alphabets and spaces.")

        elif choice == '2':
            while True:
                age = input("Enter new Age (positive integer): ")
                if is_valid_age(age):
                    employees[emp_id]["age"] = int(age)
                    print("Age updated successfully.")
                    break
                else:
                    print("Invalid age! Please enter a positive integer for age.")

        elif choice == '3':
            while True:
                department = input("Enter new Department (non-empty): ")
                if is_valid_department(department):
                    employees[emp_id]["department"] = department
                    print("Department updated successfully.")
                    break
                else:
                    print("Invalid department!")

        else:
            print("Invalid choice. Update operation canceled.")
    else:
        print("Employee ID not found. Cannot update employee.")

def search_emp():
    search_type = input("Search by Employee ID or Name (ID/Name): ").strip().lower()
    
    if search_type == "id":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print(f"Employee found: {emp_id} - {employees[emp_id]}")
        else:
            print("Employee ID not found.")
    
    elif search_type == "name":
        name = input("Enter Name (case-insensitive): ").strip().lower()
        found = False
        for emp_id, details in employees.items():
            if name in details["name"].lower():
                print(f"Employee found: {emp_id} - {details}")
                found = True
        if not found:
            print("No employees found with that name.")
    
    else:
        print("Invalid search type. Please choose either 'ID' or 'Name'.")

def sort_emp():
    sort_type = input("Sort by [1] Name, [2] Age, [3] Department: ")
    sorted_employees = list(employees.items())

    if sort_type == '1':
        sorted_employees.sort(key=lambda x: x[1]['name'])
    elif sort_type == '2':
        sorted_employees.sort(key=lambda x: x[1]['age'])
    elif sort_type == '3':
        sorted_employees.sort(key=lambda x: x[1]['department'])
    else:
        print("Invalid choice.")
        return
    for emp_id, details in sorted_employees:
        print(f"{emp_id}: {details}")

def display_menu():
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Employee")
    print("4. Search Employee")
    print("5. Sort Employees")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_emp()
        elif choice == '2':
            remove_emp()
        elif choice == '3':
            update_emp()
        elif choice == '4':
            search_emp()
        elif choice == '5':
            sort_emp()
        elif choice == '6':
            print("Exiting Employee Management System.")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
