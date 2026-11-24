"""
Question 10:
Write a Python program to accept an integer and determine whether it is positive, negative, even, odd, or zero.
"""

num = int(input("Enter an integer: "))

if num == 0:
    print("The number is Zero")
else:
    if num > 0:
        print("The number is Positive")
    else:
        print("The number is Negative")

    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")
