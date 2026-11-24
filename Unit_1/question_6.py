"""
Question 6:
Write a Python program to accept a student's percentage and display the appropriate grade using `if-elif-else` statements. Also validate that the percentage is between 0 and 100.
"""

percentage = float(input("Enter percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage! Enter a value between 0 and 100.")
elif percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")
