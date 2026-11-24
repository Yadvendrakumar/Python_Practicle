"""
Question 25:
Write a Python program to accept an integer and display all its factors. Also display the total number of factors.
"""

num = int(input("Enter a positive integer: "))
count = 0

if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Factors of", num, "are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")
            count = count + 1
    print("\nTotal number of factors:", count)
