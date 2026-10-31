"""
## Task 14: Guessing Game
Write a guessing game in Python where the user has to guess a secret number.
After every guess the program tells the user whether their number was too large or too small.
At the end the number of tries needed should be printed.

"""

secret_number = 8
guesses = 0

while True:
    guess = int(input("Guess the number: "))
    guesses += 1

    if guess > secret_number:
        print("Too large")
    elif guess < secret_number:
        print("Too small")
    else:
        print(f"Correct answer! It took {guesses} guesses.")
        break