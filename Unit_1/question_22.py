"""
Question 22:
Write a Python program to accept an integer and determine whether it is a prime number using a `for` loop.
"""

num = int(input("Enter an integer: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")
