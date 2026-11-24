"""
Question 27:
Write a Python program using nested `for` loops to display multiplication tables from 1 to 10 in a structured tabular format.
"""

print("MULTIPLICATION TABLES (1 to 10)")
print("-" * 60)

# Header row
print("     ", end="")
for j in range(1, 11):
    print(f"{j:5}", end="")
print()
print("-" * 60)

# Outer loop -> table number (row), inner loop -> multiplier (column)
for i in range(1, 11):
    print(f"{i:3} |", end="")
    for j in range(1, 11):
        print(f"{i * j:5}", end="")
    print()
