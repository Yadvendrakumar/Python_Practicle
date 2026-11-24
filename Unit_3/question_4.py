"""
Question 4 (Unit 3): Tuples, Sets and Set Operations
Write a Python program to perform the following operations using tuples and sets:
Create a tuple containing student roll numbers and display its elements.
Demonstrate tuple indexing, slicing and concatenation.
Create two sets containing student roll numbers from two different courses.
Perform union, intersection, difference and symmetric difference.
Check whether one set is a subset or superset of another set.
Add and remove elements from a set.
Use set comprehension to generate a set of squares of even numbers from a given range.
"""

print("--- Tuple ---")
rolls = (101, 102, 103, 104, 105)
for r in rolls:
    print("Roll number:", r)
print("Index 0     :", rolls[0])
print("Index -1    :", rolls[-1])
print("Slice [1:4] :", rolls[1:4])
print("Concatenate :", rolls + (106, 107))

print("\n--- Sets ---")
python_course = {101, 102, 103, 104, 105}
java_course = {103, 104, 105, 106, 107}
print("Python course:", python_course)
print("Java course  :", java_course)

print("Union                :", python_course | java_course)
print("Intersection         :", python_course & java_course)
print("Difference (P - J)   :", python_course - java_course)
print("Symmetric difference :", python_course ^ java_course)

small = {101, 102}
print("\n{101,102} is subset of Python course   :", small.issubset(python_course))
print("Python course is superset of {101,102}  :", python_course.issuperset(small))

new_roll = int(input("\nEnter roll number to add to Python course: "))
python_course.add(new_roll)
print("After add    :", python_course)
del_roll = int(input("Enter roll number to remove: "))
python_course.discard(del_roll)       # discard does not raise error if missing
print("After remove :", python_course)

print("\n--- Set comprehension ---")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
squares = {x ** 2 for x in range(start, end + 1) if x % 2 == 0}
print("Squares of even numbers:", squares)
