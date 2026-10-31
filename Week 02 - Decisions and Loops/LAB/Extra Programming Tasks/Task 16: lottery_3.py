"""## Task 16: Lottery (Three-Digit)
The program prompts the user to enter a three-digit number and determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is £10,000.
2. If all the digits in the user input match all the digits in the lottery number, the award is £3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is £1,000."""

import random

lottery = random.randint(100, 999)
guess = int(input("Enter your three-digit number: "))

l1 = lottery // 10
l2 = (lottery // 10)% 10
l3 = lottery % 10

g1 = guess // 10
g2 = (guess // 10) % 10
g3 = guess % 10

if guess == lottery:
    print(f"You have won £10,000! The lottery number was {lottery}")
elif (g1 == l1 or g1 == l2 or g1 == l3) and (g2 == l1 or g2 == l2 or g2 == l3) and (g3 == l1 or g3 == l2 or g3 == l3):
    print(f"You have won £3,000! The lottery number was {lottery}")
elif g1 in (l1, l2, l3) or g2 in (l1, l2, l3) or g3 in (l1, l2, l3):
    print(f"You have won £1,000! The lottery number was {lottery}")
else:
    print(f"You have not won. The lottery number was {lottery}")