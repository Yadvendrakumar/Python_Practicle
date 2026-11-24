"""
Question 28:
Write a Python program using nested loops to generate a number pattern for `n` rows, where `n` is entered by the user.
"""

n = int(input("Enter number of rows: "))

# Pattern (n = 5):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1, n + 1):          # outer loop -> rows
    for j in range(1, i + 1):      # inner loop -> numbers in each row
        print(j, end=" ")
    print()
