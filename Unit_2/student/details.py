"""Module for student details."""


def get_details():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    course = input("Enter course: ")
    return {"name": name, "roll": roll, "course": course}


def display_details(info):
    print("\n--- Student Details ---")
    print("Name   :", info["name"])
    print("Roll No:", info["roll"])
    print("Course :", info["course"])
