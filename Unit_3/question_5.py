"""
Question 5 (Unit 3): Dictionaries, Dictionary Comprehension and Nested Collections
Write a Python program to maintain employee information using dictionaries.
Create a dictionary containing employee ID, name, department and salary.
Add, update and delete dictionary elements.
Display dictionary keys, values and key-value pairs using appropriate dictionary methods.
Search for an employee using employee ID.
Use dictionary comprehension to create a dictionary of employees earning above a specified salary.
"""

# Nested dictionary: employee ID -> details
employees = {
    101: {"name": "Amit", "department": "IT", "salary": 50000},
    102: {"name": "Neha", "department": "HR", "salary": 40000},
    103: {"name": "Rahul", "department": "Finance", "salary": 60000},
}
print("Employees:", employees)

# Add
emp_id = int(input("\nEnter new employee ID: "))
name = input("Enter name: ")
dept = input("Enter department: ")
salary = float(input("Enter salary: "))
employees[emp_id] = {"name": name, "department": dept, "salary": salary}
print("After adding:", employees)

# Update
upd = int(input("\nEnter employee ID to update salary: "))
if upd in employees:
    employees[upd]["salary"] = float(input("Enter new salary: "))
    print("After update:", employees[upd])
else:
    print("Employee not found")

# Delete
dele = int(input("\nEnter employee ID to delete: "))
if dele in employees:
    del employees[dele]
    print("Employee deleted")
else:
    print("Employee not found")

print("\nKeys  :", list(employees.keys()))
print("Values:", list(employees.values()))
print("Items :")
for k, v in employees.items():
    print(" ", k, "->", v)

# Search
find = int(input("\nEnter employee ID to search: "))
print("Found:" if find in employees else "Not found", employees.get(find, ""))

# Dictionary comprehension
limit = float(input("\nEnter salary limit: "))
rich = {k: v for k, v in employees.items() if v["salary"] > limit}
print(f"Employees earning above {limit}:", rich)
