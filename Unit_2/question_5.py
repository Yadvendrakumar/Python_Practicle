"""
Question 5 (Unit 2): User-Defined Modules and Packages
Write a Python program to create and use user-defined modules and packages.
Create a module named arithmetic.py containing functions for addition, subtraction, multiplication and division.
Import the entire module and access its functions.
Import selected functions using from ... import.
Create a package named student containing separate modules for student details and student results.
Create an __init__.py file to initialize the package and expose selected functions.
Import the package modules into the main program and execute their functions.

Files used: arithmetic.py, student/__init__.py, student/details.py, student/results.py
"""

import arithmetic                          # import the entire module
from arithmetic import multiply, divide    # import selected functions

import student                             # package (runs student/__init__.py)
from student import details, results       # import modules of the package

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\n--- Using whole module (arithmetic.function) ---")
print("Addition   :", arithmetic.add(a, b))
print("Subtraction:", arithmetic.subtract(a, b))

print("\n--- Using from ... import ---")
print("Multiplication:", multiply(a, b))
print("Division      :", divide(a, b))

print("\n--- Using package 'student' ---")
info = student.get_details()               # function exposed by __init__.py
student.display_details(info)

n = int(input("\nEnter number of subjects: "))
marks = [float(input(f"Enter marks of subject {i}: ")) for i in range(1, n + 1)]
total, percentage, grade = results.calculate_result(marks)   # via module
results.display_result(total, percentage, grade)
