"""
Question 30:
Write a Python program to accept the marks of N students and calculate the class average, highest marks, lowest marks, number of passed and failed students, and number of students scoring above 75%.
"""

# Marks are out of 100. Pass marks = 40.
n = int(input("Enter number of students: "))

total = 0
highest = 0
lowest = 100
passed = 0
failed = 0
above_75 = 0

for i in range(1, n + 1):
    marks = float(input("Enter marks of student " + str(i) + ": "))
    total = total + marks

    if i == 1 or marks > highest:
        highest = marks
    if i == 1 or marks < lowest:
        lowest = marks

    if marks >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

    if marks > 75:
        above_75 = above_75 + 1

if n > 0:
    print("\nClass Average            :", total / n)
    print("Highest Marks            :", highest)
    print("Lowest Marks             :", lowest)
    print("Passed Students          :", passed)
    print("Failed Students          :", failed)
    print("Students scoring above 75:", above_75)
else:
    print("No students entered.")
