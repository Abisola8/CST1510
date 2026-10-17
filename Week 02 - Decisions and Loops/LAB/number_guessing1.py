"""
## Number Guessing Game

"""

secret_number = 8
guesses = 0

while True:
    guess = int(input("Guess the number: "))
    guesses += 1

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"Correct answer! It took {guesses} guesses.")
        break