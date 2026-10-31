"""## Task 17: Find the Two Highest Scores
Write a program that prompts the user to enter the number of students and
each student's score and displays the highest and second highest scores."""

students = int(input("Enter the number of students: "))

highest = 0
second_highest = 0

for i in range(students):
    score = int(input("Enter the score of the student: "))

    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest:
        second_highest = score

print(f"The highest score is {highest}, the second highest score is {second_highest}.")