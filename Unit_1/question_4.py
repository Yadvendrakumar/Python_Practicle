"""
Question 4:
Write a Python program to accept a time duration in seconds and convert it into hours, minutes, and seconds.
"""

total_seconds = int(input("Enter time in seconds: "))

hours = total_seconds // 3600                # full hours
minutes = (total_seconds % 3600) // 60       # remaining seconds -> minutes
seconds = total_seconds % 60                 # leftover seconds

print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
