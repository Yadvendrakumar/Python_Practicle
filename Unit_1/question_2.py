"""
Question 2:
Write a Python program to accept an employee's basic salary and calculate DA, HRA, gross salary, tax deduction, and net salary.
"""

basic = float(input("Enter Basic Salary: "))

da = 0.20 * basic            # Dearness Allowance = 20% of basic
hra = 0.15 * basic           # House Rent Allowance = 15% of basic
gross = basic + da + hra     # Gross salary
tax = 0.10 * gross           # Tax deduction = 10% of gross
net = gross - tax            # Net salary

print("DA            :", da)
print("HRA           :", hra)
print("Gross Salary  :", gross)
print("Tax Deduction :", tax)
print("Net Salary    :", net)
