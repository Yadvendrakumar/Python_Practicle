"""
Question 21:
Write a Python program to implement a number guessing game in which the user repeatedly enters guesses until the correct number is found. Display whether each guess is too high or too low.
"""

import random

secret = random.randint(1, 100)       # computer picks a number between 1 and 100
attempts = 0

print("Guess the number between 1 and 100")
guess = int(input("Enter your guess: "))
attempts = attempts + 1

while guess != secret:
    if guess > secret:
        print("Too High! Try again.")
    else:
        print("Too Low! Try again.")
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

print("Congratulations! You guessed the number", secret, "in", attempts, "attempts.")
