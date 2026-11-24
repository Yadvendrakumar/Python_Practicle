"""
Question 1:
Write a Python program to accept the marks obtained by a student in five subjects and calculate the total marks, average marks, and percentage.
"""

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5          # total of all subjects
average = total / 5                     # average marks
percentage = (total / 500) * 100        # each subject is out of 100

print("Total Marks     :", total)
print("Average Marks   :", average)
print("Percentage      :", percentage, "%")
