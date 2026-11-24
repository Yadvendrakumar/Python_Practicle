"""
Question 11:
Write a Python program to accept a person's age, monthly income, and credit score and determine whether the person is eligible for a loan based on specified conditions.
"""

# Conditions: age 21-60, monthly income >= 25000, credit score >= 700
age = int(input("Enter age: "))
income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

if age >= 21 and age <= 60 and income >= 25000 and credit_score >= 700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
