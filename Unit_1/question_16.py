"""
Question 16:
Write a Python program to accept an integer and reverse its digits using a `while` loop.
"""

num = int(input("Enter an integer: "))
n = abs(num)
reverse = 0

while n != 0:
    digit = n % 10                    # extract last digit
    reverse = reverse * 10 + digit    # add it to reversed number
    n = n // 10                       # remove last digit

if num < 0:
    reverse = -reverse

print("Reversed number:", reverse)
