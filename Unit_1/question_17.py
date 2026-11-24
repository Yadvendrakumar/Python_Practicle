"""
Question 17:
Write a Python program to accept an integer and determine whether it is a palindrome using a `while` loop.
"""

num = int(input("Enter an integer: "))
n = num
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if num >= 0 and num == reverse:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")
