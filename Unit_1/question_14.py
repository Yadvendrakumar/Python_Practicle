"""
Question 14:
Write a Python program to accept a person's annual income and calculate the tax payable according to different income slabs.
"""

# Slabs:
#   Up to 2,50,000          -> No tax
#   2,50,001 - 5,00,000     -> 5%
#   5,00,001 - 10,00,000    -> 20%
#   Above 10,00,000         -> 30%
income = float(input("Enter annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 250000 * 0.05 + (income - 500000) * 0.20
else:
    tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30

print("Tax Payable: Rs.", round(tax, 2))
