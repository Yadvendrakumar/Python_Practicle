"""
Question 2 (Unit 2): Variable-Length Arguments and Return Statement
Write a Python program to calculate the total marks, average marks and highest marks of a student.
Accept student name and subject details.
Use *args to accept marks of multiple subjects.
Use **kwargs to accept additional student information such as roll number and class.
Return total, average and highest marks from a function.
Display the student result using formatted output.
"""


def student_result(name, *marks, **info):
    total = sum(marks)                 # *args -> tuple of marks
    average = total / len(marks)
    highest = max(marks)
    print("\n" + "=" * 35)
    print(f"{'STUDENT RESULT':^35}")
    print("=" * 35)
    print(f"{'Name':<15}: {name}")
    for key, value in info.items():    # **kwargs -> dictionary
        print(f"{key.capitalize():<15}: {value}")
    print("=" * 35)
    return total, average, highest     # returns a tuple


name = input("Enter student name: ")
roll = input("Enter roll number: ")
cls = input("Enter class: ")
n = int(input("Enter number of subjects: "))

marks_list = []
for i in range(1, n + 1):
    marks_list.append(float(input(f"Enter marks of subject {i}: ")))

total, average, highest = student_result(name, *marks_list, roll_no=roll, student_class=cls)

print(f"{'Total Marks':<15}: {total:.2f}")
print(f"{'Average Marks':<15}: {average:.2f}")
print(f"{'Highest Marks':<15}: {highest:.2f}")
print("=" * 35)
