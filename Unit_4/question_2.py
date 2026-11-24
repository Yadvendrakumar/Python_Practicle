"""
Question 2 (Unit 4): File Handling - Read, Write and Append
Write a Python program to perform the following operations on a text file named student.txt:
Create and open a file in write mode.
Accept and write student details into the file.
Read and display the complete file contents.
Append additional student records without deleting existing records.
Read the file line by line.
Display all lines using appropriate file methods.
Close the file using the close() method.
"""

# Write mode (creates file / overwrites old content)
f = open("student.txt", "w")
n = int(input("How many students to write? "))
for i in range(n):
    roll = input(f"Student {i + 1} roll number: ")
    name = input(f"Student {i + 1} name: ")
    course = input(f"Student {i + 1} course: ")
    f.write(f"{roll},{name},{course}\n")
f.close()

# Read complete file
f = open("student.txt", "r")
print("\n--- Complete file contents ---")
print(f.read())
f.close()

# Append mode (old records are kept)
f = open("student.txt", "a")
m = int(input("How many more students to append? "))
for i in range(m):
    roll = input(f"Extra student {i + 1} roll number: ")
    name = input(f"Extra student {i + 1} name: ")
    course = input(f"Extra student {i + 1} course: ")
    f.write(f"{roll},{name},{course}\n")
f.close()

# Read line by line
f = open("student.txt", "r")
print("\n--- Reading line by line (readline) ---")
line = f.readline()
while line:
    print(line.strip())
    line = f.readline()
f.close()

# Display all lines with readlines()
f = open("student.txt", "r")
print("\n--- All lines using readlines() ---")
for line in f.readlines():
    print(line.strip())
f.close()
print("\nFile closed:", f.closed)
