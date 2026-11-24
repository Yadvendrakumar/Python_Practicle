"""
Question 4 (Unit 4): Python Standard Libraries - random module
Write a Python program to demonstrate the random library:
Generate random integers, select a random element from a list and shuffle list elements.
"""

import random

print("Random integer (1-100):", random.randint(1, 100))
print("Random integer from range(0,50,5):", random.randrange(0, 50, 5))

fruits = ["apple", "banana", "mango", "orange", "grapes"]
print("Random choice from list:", random.choice(fruits))

random.shuffle(fruits)
print("List after shuffle     :", fruits)
