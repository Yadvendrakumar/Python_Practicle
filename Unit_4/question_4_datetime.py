"""
Question 4 (Unit 4): Python Standard Libraries - datetime module
Write a Python program to demonstrate the datetime library:
Display the current date and time, extract day, month and year,
and calculate the difference between two dates.
"""

from datetime import datetime, date

now = datetime.now()
print("Current date and time:", now.strftime("%d-%m-%Y %H:%M:%S"))
print("Day  :", now.day)
print("Month:", now.month)
print("Year :", now.year)

d1 = date.fromisoformat(input("Enter first date (YYYY-MM-DD): "))
d2 = date.fromisoformat(input("Enter second date (YYYY-MM-DD): "))
diff = d2 - d1
print("Difference between the two dates:", abs(diff.days), "days")
