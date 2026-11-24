"""
Question 3 (Unit 4): File Methods and Exception Handling
Write a Python program to demonstrate various file methods and file-related exception handling.
Open an existing text file in read mode.
Use read(), readline() and readlines() to retrieve file contents.
Demonstrate tell() to identify the current file position.
Use seek() to move the file pointer to a specified position.
Display the file name and file mode.
Handle FileNotFoundError and PermissionError.
Use try, except, else and finally appropriately while performing file operations.
"""

filename = input("Enter file name to open (e.g. student.txt): ")
f = None

try:
    f = open(filename, "r")
except FileNotFoundError:
    print("Error: File not found. Run Unit_4/question_2.py first to create student.txt")
except PermissionError:
    print("Error: You do not have permission to open this file")
else:
    print("File name:", f.name)
    print("File mode:", f.mode)

    print("\nread(10)   :", repr(f.read(10)))
    print("tell()     :", f.tell(), "(current position)")

    f.seek(0)
    print("\nAfter seek(0), tell():", f.tell())
    print("readline() :", repr(f.readline()))
    print("tell()     :", f.tell())

    f.seek(0)
    print("\nreadlines():", f.readlines())

    f.seek(5)
    print("\nAfter seek(5), read(5):", repr(f.read(5)))
finally:
    if f is not None:
        f.close()
        print("\nFile closed successfully")
    print("finally block executed")
