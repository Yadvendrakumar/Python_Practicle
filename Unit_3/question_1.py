"""
Question 1 (Unit 3): String Operations and String Methods
Write a Python program to accept a sentence from the user and perform the following operations:
Find the length of the string.
Convert the string into uppercase and lowercase.
Remove leading and trailing spaces.
Replace a specified word with another word.
Count the occurrences of a particular character.
Check whether the string starts or ends with a specified substring.
Demonstrate string concatenation, repetition and membership operators.
"""

s = input("Enter a sentence: ")

print("Length            :", len(s))
print("Uppercase         :", s.upper())
print("Lowercase         :", s.lower())
print("After strip()     :", s.strip())

old = input("Enter word to replace: ")
new = input("Enter new word: ")
print("After replace     :", s.replace(old, new))

ch = input("Enter a character to count: ")
print(f"'{ch}' occurs {s.count(ch)} time(s)")

start = input("Enter substring to check at start: ")
end = input("Enter substring to check at end: ")
print("Starts with", start, ":", s.strip().startswith(start))
print("Ends with", end, ":", s.strip().endswith(end))

print("\n--- Concatenation, repetition, membership ---")
print("Concatenation :", s.strip() + " - Python")
print("Repetition    :", "Hi! " * 3)
print(f"'{old}' in sentence     :", old in s)
print(f"'{old}' not in sentence :", old not in s)
