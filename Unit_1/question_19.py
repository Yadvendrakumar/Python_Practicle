"""
Question 19:
Write a Python program to accept an integer and find the number of digits, largest digit, and smallest digit using a `while` loop.
"""

num = int(input("Enter an integer: "))
n = abs(num)

if n == 0:
    count = 1
    largest = 0
    smallest = 0
else:
    count = 0
    largest = 0
    smallest = 9
    while n != 0:
        digit = n % 10
        count = count + 1
        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit
        n = n // 10

print("Number of digits :", count)
print("Largest digit    :", largest)
print("Smallest digit   :", smallest)
