"""
Question 4 (Unit 4): Python Standard Libraries - math module
Write a Python program to demonstrate the math library:
Calculate square root, factorial, power, ceiling and floor of a number.
"""

import math

n = float(input("Enter a number: "))
print("Square root :", math.sqrt(n))
print("Ceiling     :", math.ceil(n))
print("Floor       :", math.floor(n))
print("Power (n^2) :", math.pow(n, 2))
print("Factorial   :", math.factorial(int(n)) if n >= 0 else "Not defined for negative numbers")
