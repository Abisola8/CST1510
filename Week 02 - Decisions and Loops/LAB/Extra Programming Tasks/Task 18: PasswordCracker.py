"""## Task 18: Password Cracker
Write a program to print the accuracy of a password guess.

For example: The actual password is `MDX123` while a user tried `MDX321` or `mdx123`, the program should tell how accurately the password was guessed, in this case it should be `50%` accuracy.
If a user enters `MDX124`, the output should be `83%` and in case of `123MDX` the output should be `0%`.

Points to keep in mind while calculating the accuracy:
- a) case of the letters entered
- b) order of the letters

If a password is accurately guessed, the output should state `Password cracked!`"""

password = "MDX123"
guess = input("Enter your password guess: ")

characters_matched = 0

for i in range(len(password)):
    if i < len(guess) and password[i].lower() == guess[i].lower():
        characters_matched += 1

percent = (characters_matched / len(password)) * 100

if guess.lower() == password.lower():
    print("Password cracked!")
else:
    print(f"Accuracy: {percent:.0f}%")
