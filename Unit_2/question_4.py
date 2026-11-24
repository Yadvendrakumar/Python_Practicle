"""
Question 4 (Unit 2): Scope, Lifetime and Lambda Functions
Write a Python program to demonstrate scope and lifetime of variables.
Create global and local variables.
Demonstrate the use of the global keyword.
Show how local variables are accessed within functions.
Explain the lifetime of local and global variables through program execution.
Create lambda functions to calculate square, cube, maximum of two numbers and addition of two numbers.
"""

counter = 10        # global variable: lives until the program ends


def show_local():
    local_var = 5   # local variable: created when function is called
    print("Inside show_local(): local_var =", local_var)
    print("Inside show_local(): global counter (read) =", counter)
    # local_var is destroyed when the function ends


def change_global():
    global counter  # 'global' keyword lets us modify the global variable
    counter = counter + 1
    print("Inside change_global(): counter =", counter)


def shadow_global():
    counter = 100   # this is a NEW local variable, global is untouched
    print("Inside shadow_global(): local counter =", counter)


print("Global counter at start:", counter)
show_local()
change_global()
shadow_global()
print("Global counter at end  :", counter)

try:
    print(local_var)   # lifetime of local_var ended with show_local()
except NameError as e:
    print("Error: local_var is not accessible outside the function ->", e)

print("\n--- Lambda functions ---")
square = lambda x: x * x
cube = lambda x: x ** 3
maximum = lambda a, b: a if a > b else b
addition = lambda a, b: a + b

n = int(input("Enter a number: "))
m = int(input("Enter another number: "))
print("Square of", n, "=", square(n))
print("Cube of", n, "=", cube(n))
print("Maximum of", n, "and", m, "=", maximum(n, m))
print("Addition of", n, "and", m, "=", addition(n, m))
