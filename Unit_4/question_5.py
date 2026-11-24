"""
Question 5 (Unit 4): Command-Line Arguments
Write a Python program to accept two numbers and an operation through command-line arguments.
Accept two numbers as command-line arguments.
Accept an arithmetic operator (+, -, *, /) as another argument.
Perform the specified arithmetic operation.
Display the calculated result.

Usage:  python question_5.py 10 5 +
        python question_5.py 10 5 "*"      (quote * and use it carefully in the shell)
"""

import sys

if len(sys.argv) != 4:
    print("Usage: python question_5.py <num1> <num2> <operator>")
    sys.exit(1)

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
except ValueError:
    print("Error: first two arguments must be numbers")
    sys.exit(1)

op = sys.argv[3]

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", "Division by zero not possible" if num2 == 0 else num1 / num2)
else:
    print("Invalid operator. Use +, -, * or /")
