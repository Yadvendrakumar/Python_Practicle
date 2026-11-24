"""
Question 8:
Write a Python program to accept three sides of a triangle, determine whether they form a valid triangle, and if valid, classify it as Equilateral, Isosceles, or Scalene.
"""

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

# Triangle is valid if sum of any two sides is greater than the third
if a > 0 and b > 0 and c > 0 and (a + b > c) and (b + c > a) and (a + c > b):
    if a == b == c:
        print("Valid triangle: Equilateral")
    elif a == b or b == c or a == c:
        print("Valid triangle: Isosceles")
    else:
        print("Valid triangle: Scalene")
else:
    print("Not a valid triangle")
