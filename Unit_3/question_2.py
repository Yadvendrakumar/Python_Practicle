"""
Question 2 (Unit 3): String Slicing and String Formatting
Write a Python program to accept a student's full name, email address and mobile number.
Extract the first name and last name using string slicing.
Reverse the student's name using slicing.
Extract the username and domain from the email address.
Extract the last four digits of the mobile number.
Display the student information using f-string formatting and other string formatting techniques.
Demonstrate positive and negative indexing.
"""

full_name = input("Enter full name (first last): ").strip()
email = input("Enter email address: ").strip()
mobile = input("Enter 10-digit mobile number: ").strip()

space = full_name.index(" ")
first_name = full_name[:space]            # slicing
last_name = full_name[space + 1:]
reversed_name = full_name[::-1]

at = email.index("@")
username = email[:at]
domain = email[at + 1:]

last4 = mobile[-4:]                       # negative slicing

print("\n--- Slicing results ---")
print("First name   :", first_name)
print("Last name    :", last_name)
print("Reversed name:", reversed_name)
print("Username     :", username)
print("Domain       :", domain)
print("Last 4 digits:", last4)

print("\n--- Indexing ---")
print("First character (index 0)  :", full_name[0])
print("Last character (index -1)  :", full_name[-1])
print("Second last (index -2)     :", full_name[-2])

print("\n--- Formatting ---")
print(f"f-string   : Name={full_name}, Email={email}, Mobile=XXXXXX{last4}")
print("format()   : Name={}, Email={}".format(full_name, email))
print("Old style  : Name=%s, Mobile=XXXXXX%s" % (full_name, last4))
print(f"Aligned    : |{first_name:<10}|{last_name:^10}|{last4:>6}|")
