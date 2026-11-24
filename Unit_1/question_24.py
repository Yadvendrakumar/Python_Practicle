"""
Question 24:
Write a Python program to accept the number of terms and generate the Fibonacci series using a `for` loop. Also calculate the sum of the generated terms.
"""

n = int(input("Enter number of terms: "))
a = 0
b = 1
total = 0

print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    total = total + a
    a, b = b, a + b       # shift to next pair

print("\nSum of the terms:", total)
