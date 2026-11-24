"""
Question 1 (Unit 4): Exception Handling
Write a Python program to demonstrate exception handling for the following situations:
Handle division by zero using ZeroDivisionError.
Handle invalid numerical input using ValueError.
Handle invalid list index using IndexError.
Use multiple except blocks to handle different exceptions.
Demonstrate the use of else when no exception occurs.
Demonstrate the use of finally for executing statements irrespective of exceptions.
Use raise to generate an exception when the entered age is less than 18.
"""

numbers = [10, 20, 30, 40, 50]

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    idx = int(input("Enter list index (0-4): "))
    result = a / b
    value = numbers[idx]
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Please enter valid integer numbers only")
except IndexError:
    print("Error: List index out of range")
else:
    print("Result of division:", result)
    print("List element      :", value)
    print("No exception occurred")
finally:
    print("finally block: this always executes")

print("\n--- Using raise ---")
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age is less than 18, not eligible")
    print("You are eligible")
except ValueError as e:
    print("Error:", e)
