"""
Question 13:
Write a Python program to simulate an ATM withdrawal by accepting a PIN, account balance, and withdrawal amount. Validate the transaction and display an appropriate message.
"""

correct_pin = 1234

pin = int(input("Enter PIN: "))
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if pin != correct_pin:
    print("Incorrect PIN. Transaction cancelled.")
elif amount <= 0:
    print("Invalid amount. Enter a positive amount.")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100.")
elif amount > balance:
    print("Insufficient balance.")
else:
    balance = balance - amount
    print("Withdrawal successful!")
    print("Remaining balance:", balance)
