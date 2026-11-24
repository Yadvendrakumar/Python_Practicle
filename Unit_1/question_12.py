"""
Question 12:
Write a Python program to accept marks obtained in Mathematics, Physics, and Chemistry and determine whether a student is eligible for admission based on subject-wise and overall percentage requirements.
"""

# Conditions: each subject >= 50 marks AND overall percentage >= 60
maths = float(input("Enter marks in Mathematics: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))

total = maths + physics + chemistry
percentage = (total / 300) * 100
print("Overall Percentage:", round(percentage, 2), "%")

if maths >= 50 and physics >= 50 and chemistry >= 50 and percentage >= 60:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")
