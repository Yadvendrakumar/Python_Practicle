"""
Question 20:
Write a Python program to accept an integer and determine whether it is an Armstrong number.
"""

# Armstrong number: sum of (each digit ^ number of digits) == the number
# Example: 153 = 1^3 + 5^3 + 3^3
num = int(input("Enter an integer: "))
temp = num
num_digits = len(str(abs(num)))
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** num_digits
    temp = temp // 10

if num >= 0 and total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
