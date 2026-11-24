"""
Question 26:
Write a Python program to accept two positive integers and calculate their GCD and LCM using iterative statements.
"""

a = int(input("Enter first positive integer: "))
b = int(input("Enter second positive integer: "))

if a <= 0 or b <= 0:
    print("Please enter positive integers only.")
else:
    x = a
    y = b
    while y != 0:          # Euclidean algorithm
        x, y = y, x % y
    gcd = x
    lcm = (a * b) // gcd   # LCM = (a * b) / GCD

    print("GCD:", gcd)
    print("LCM:", lcm)
