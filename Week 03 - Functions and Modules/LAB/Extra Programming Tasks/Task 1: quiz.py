""" 
## Task 1: Quiz
Suppose you want to develop a program to help a first grader practice addition, subtraction, multiplication, division, exponent or remainder. The user should have the option of choosing which mathematical operation they wish to practice. The program randomly generates two single-digit integers, number1 and number2, and of course the user will provide the answer to the question.

The program should include:
- A menu allowing the student to choose the operation they want to practice (ideally included in function names or main).
- Functions for each of the mathematical operations.
- A score calculating correct answers.
- Error messages for situations such as division by zero.
- Functionality to keep practicing until the user decides otherwise.
"""
import random

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: You can't divide by zero.")
        return None
    return n1 / n2

def exponent(n1, n2):
    return n1 ** n2

def remainder(n1, n2):
    if n2 == 0:
        print("Error: You can't divide by zero.")
        return None
    return n1 % n2

score = 0
questions = 0

keep_going = True

while keep_going:
    operator = input("Enter an operator that you want to practice (+ - * / ** %): ")

    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)

    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        result = divide(n1, n2)
    elif operator == "**":
        result = exponent(n1, n2)
    elif operator == "%":
        result = remainder(n1, n2)
    else:
        print("Invalid operator")
        continue

    guess = float(input(f"What is {n1} {operator} {n2}? "))
    
    if guess == result:
            print("Correct!")
            score += 1
            questions += 1
    else:
        print("Incorrect.")
        questions += 1
    
    print(f"{n1}{operator}{n2} = {result}")
    
    choice = input("Type 'y' to continue or 'q' to quit: ")
    if choice == 'y':
        print(guess)
    elif choice == 'q':
        print(f"{n1}{operator}{n2} = {result}")
        keep_going = False
        print(f"You answered {score} out of {questions} questions correctly.")
    else:
        print("Invalid choice. Exiting the program.")
        keep_going = False
        print(f"You answered {score} out of {questions} questions correctly.")

    