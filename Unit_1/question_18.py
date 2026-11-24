"""
Question 18:
Write a Python program to accept an integer and calculate the sum and product of all its digits using a `while` loop.
"""

num = int(input("Enter an integer: "))
n = abs(num)
digit_sum = 0
digit_product = 1

if n == 0:
    digit_product = 0

while n != 0:
    digit = n % 10
    digit_sum = digit_sum + digit
    digit_product = digit_product * digit
    n = n // 10

print("Sum of digits     :", digit_sum)
print("Product of digits :", digit_product)
