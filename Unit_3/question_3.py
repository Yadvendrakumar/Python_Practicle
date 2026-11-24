"""
Question 3 (Unit 3): List Operations and List Comprehension
Write a Python program to perform the following operations on a list of integers:
Create a list of n numbers.
Insert and remove elements at specified positions.
Sort the list in ascending and descending order.
Find the maximum, minimum and sum of list elements.
Demonstrate list concatenation, repetition, indexing and membership operations.
Display even numbers, odd numbers and squares of numbers using list comprehension.
Demonstrate appropriate list methods such as append(), extend(), insert(), remove(), pop(), sort() and reverse().
"""

n = int(input("Enter how many numbers: "))
nums = [int(input(f"Enter number {i + 1}: ")) for i in range(n)]
print("List:", nums)

nums.append(100)
print("After append(100)       :", nums)
nums.extend([7, 8])
print("After extend([7, 8])    :", nums)

pos = int(input("Enter position to insert at: "))
val = int(input("Enter value to insert: "))
nums.insert(pos, val)
print("After insert            :", nums)

rem = int(input("Enter value to remove: "))
if rem in nums:
    nums.remove(rem)
    print("After remove            :", nums)
else:
    print(rem, "not found in list")

print("pop() removed           :", nums.pop(), "->", nums)

nums.sort()
print("Ascending               :", nums)
nums.sort(reverse=True)
print("Descending              :", nums)
nums.reverse()
print("After reverse()         :", nums)

print("Maximum:", max(nums), "| Minimum:", min(nums), "| Sum:", sum(nums))

print("\n--- Concatenation, repetition, indexing, membership ---")
print("Concatenation :", nums + [1, 2])
print("Repetition    :", [0, 1] * 3)
print("First element :", nums[0], "| Last element:", nums[-1])
print("Is 100 in list?", 100 in nums)

print("\n--- List comprehension ---")
print("Even numbers :", [x for x in nums if x % 2 == 0])
print("Odd numbers  :", [x for x in nums if x % 2 != 0])
print("Squares      :", [x ** 2 for x in nums])
