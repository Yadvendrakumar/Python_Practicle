"""
Question 1 (Unit 2): Functions and Function Arguments
Write a Python program to perform arithmetic operations using user-defined functions.
Define separate functions for addition, subtraction, multiplication and division.
Pass numbers using positional arguments.
Demonstrate keyword arguments while calling the functions.
Use default arguments to assign a default operation value.
Return the calculated result from each function.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b


# Default argument: if no operation is given, 'add' is used
def calculate(a, b, operation="add"):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    return "Invalid operation"


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("\n--- Positional arguments ---")
print("Addition       :", add(x, y))
print("Subtraction    :", subtract(x, y))
print("Multiplication :", multiply(x, y))
print("Division       :", divide(x, y))

print("\n--- Keyword arguments (order does not matter) ---")
print("Subtraction (b first):", subtract(b=y, a=x))
print("Division (b first)   :", divide(b=y, a=x))

print("\n--- Default argument ---")
print("calculate(x, y)                    :", calculate(x, y))
print("calculate(x, y, 'multiply')        :", calculate(x, y, "multiply"))
print("calculate(a=x, b=y, operation='divide'):", calculate(a=x, b=y, operation="divide"))
