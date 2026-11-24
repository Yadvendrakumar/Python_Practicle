"""
Question 23:
Write a Python program to accept two integers representing a range and display all prime numbers within that range. Also display the total number of prime numbers found.
"""

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
count = 0

print("Prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count = count + 1

print("\nTotal prime numbers found:", count)
