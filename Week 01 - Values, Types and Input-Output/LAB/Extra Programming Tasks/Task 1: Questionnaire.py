"""
Task 1: Questionnaire
Write a program that asks for name, interest, nationality, course, and programming experience, then prints a formatted summary using escape sequences (`\n`, `\t`).

**Example Output:**
```
User Information:
	Name: Alice
	Interest: Security
	Nationality: UK
	Course: Cyber
	Experience: Beginner
```
"""

name = input("What is your name? ")
interest = input("What is your interest? ")
nationality = input("What is your nationality? ")
course = input("What course are you studying? ")
experience = input("How much experience do you have? ")

print(f"User Information:\n \tName: {name}\n \tInterest: {interest}\n \tNationality: {nationality}\n \tCourse: {course}\n \tExperience: {experience}")