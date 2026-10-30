"""
## Task 1: Password Strength Checker
**Scenario:** You are a junior security analyst at a company. Employees often choose weak passwords, so you need to create a simple program to check password strength. Since you only know the basics of programming, your program will use simple rules.

**Requirements:**
1. Ask the user to enter a password.
2. If the password has fewer than 8 characters, print "Weak".
3. If the password has 8 or more characters, print "Moderate".
4. If the password has 12 or more characters, print "Strong".
"""

password = input("Enter your password: ")

if len(password) >= 12:
    print("Strong")
elif len(password) >= 8:
    print("Moderate")
else:
    print("Weak")