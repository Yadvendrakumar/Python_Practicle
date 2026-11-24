"""
Question 5:
Write a Python program to accept the price and quantity of three products and calculate the subtotal, discount, GST, and final payable amount.
"""

p1 = float(input("Enter price of product 1: "))
q1 = int(input("Enter quantity of product 1: "))
p2 = float(input("Enter price of product 2: "))
q2 = int(input("Enter quantity of product 2: "))
p3 = float(input("Enter price of product 3: "))
q3 = int(input("Enter quantity of product 3: "))

subtotal = (p1 * q1) + (p2 * q2) + (p3 * q3)
discount = 0.10 * subtotal                 # 10% discount
after_discount = subtotal - discount
gst = 0.18 * after_discount                # 18% GST on discounted amount
final_amount = after_discount + gst

print("Subtotal             :", subtotal)
print("Discount (10%)       :", discount)
print("GST (18%)            :", gst)
print("Final Payable Amount :", final_amount)
