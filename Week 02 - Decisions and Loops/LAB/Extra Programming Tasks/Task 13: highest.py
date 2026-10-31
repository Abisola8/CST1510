"""## Task 13: Find the Highest Score
Write a program that prompts the user to enter the number of students and each student's name
and score and displays the student name and highest score."""

students = int(input("Enter the number of students: "))

highest_name = ""
highest_score = 0

for i in range(students):
    name = input("Enter the name of the student: ")
    score = int(input("Enter the score of the student: "))

    if score > highest_score:
        highest_score = score
        highest_name = name

print(f"The student with the highest score is {highest_name}, the score is {highest_score}.")