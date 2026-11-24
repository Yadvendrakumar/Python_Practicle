"""
Question 3 (Unit 2): Recursive Functions
Write a Python program to perform the following operations using recursive functions:
Calculate factorial of a given number.
Generate Fibonacci series up to n terms.
"""


def factorial(n):
    if n == 0 or n == 1:               # base case
        return 1
    return n * factorial(n - 1)        # recursive case


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number for factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial of {num} = {factorial(num)}")

terms = int(input("Enter number of terms for Fibonacci series: "))
print("Fibonacci series:", end=" ")
for i in range(terms):
    print(fibonacci(i), end=" ")
print()
