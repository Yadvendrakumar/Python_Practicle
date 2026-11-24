"""Module for student results."""


def calculate_result(marks):
    total = sum(marks)
    percentage = total / len(marks)
    grade = "Pass" if percentage >= 40 else "Fail"
    return total, percentage, grade


def display_result(total, percentage, grade):
    print("\n--- Student Result ---")
    print("Total     :", total)
    print("Percentage:", round(percentage, 2))
    print("Result    :", grade)
