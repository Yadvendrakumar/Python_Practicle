"""
Question 15:
Write a Python program to accept monthly mobile data usage in GB and calculate the total bill according to specified usage slabs.
"""

# Slabs:
#   Up to 2 GB      -> Fixed Rs 199
#   2 - 5 GB        -> Rs 50 per extra GB
#   5 - 10 GB       -> Rs 40 per extra GB
#   Above 10 GB     -> Rs 30 per extra GB
usage = float(input("Enter data usage in GB: "))

if usage <= 2:
    bill = 199
elif usage <= 5:
    bill = 199 + (usage - 2) * 50
elif usage <= 10:
    bill = 199 + 3 * 50 + (usage - 5) * 40
else:
    bill = 199 + 3 * 50 + 5 * 40 + (usage - 10) * 30

print("Total Bill: Rs.", round(bill, 2))
