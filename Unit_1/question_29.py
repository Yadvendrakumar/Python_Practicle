"""
Question 29:
Write a Python program to create a menu-driven mathematical application with options to check Prime, Palindrome, Armstrong, Factorial, Fibonacci Series, and Exit. The menu should be displayed repeatedly until the user selects Exit.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(num):
    n = num
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    return num == reverse


def is_armstrong(num):
    temp = num
    power = len(str(num))
    total = 0
    while temp > 0:
        total = total + (temp % 10) ** power
        temp = temp // 10
    return total == num


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


while True:
    print("\n========== MENU ==========")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        n = int(input("Enter a number: "))
        if is_prime(n):
            print(n, "is a Prime number")
        else:
            print(n, "is not a Prime number")
    elif choice == 2:
        n = int(input("Enter a number: "))
        if is_palindrome(n):
            print(n, "is a Palindrome")
        else:
            print(n, "is not a Palindrome")
    elif choice == 3:
        n = int(input("Enter a number: "))
        if is_armstrong(n):
            print(n, "is an Armstrong number")
        else:
            print(n, "is not an Armstrong number")
    elif choice == 4:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers")
        else:
            print("Factorial of", n, "is", factorial(n))
    elif choice == 5:
        n = int(input("Enter number of terms: "))
        print("Fibonacci Series:")
        fibonacci(n)
    elif choice == 6:
        print("Thank you! Exiting program.")
        break
    else:
        print("Invalid choice! Please select between 1 and 6.")
