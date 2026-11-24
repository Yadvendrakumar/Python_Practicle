"""
Question 3:
Write a Python program to accept the number of electricity units consumed by a consumer and calculate the electricity bill according to different consumption slabs.
"""

# Slabs:
#   First 100 units  -> Rs 3.0 per unit
#   Next 100 units   -> Rs 4.5 per unit
#   Next 100 units   -> Rs 6.0 per unit
#   Above 300 units  -> Rs 7.5 per unit
units = float(input("Enter units consumed: "))

if units < 0:
    print("Invalid units!")
else:
    if units <= 100:
        bill = units * 3.0
    elif units <= 200:
        bill = 100 * 3.0 + (units - 100) * 4.5
    elif units <= 300:
        bill = 100 * 3.0 + 100 * 4.5 + (units - 200) * 6.0
    else:
        bill = 100 * 3.0 + 100 * 4.5 + 100 * 6.0 + (units - 300) * 7.5

    print("Electricity Bill: Rs.", round(bill, 2))
