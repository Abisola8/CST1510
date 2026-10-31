"""## Task 15: Lottery (Two-Digit)
Suppose you want to develop a program to play a lottery.

The program randomly generates a two-digit number, prompts the user to enter a two-digit number, and determines whether the user wins according to the following rules:
1. If the user's input matches the lottery in the exact order, the award is £10,000.
2. If all the digits in the user's input match all the digits in the lottery number, the award is £3,000.
3. If one digit in the user's input matches a digit in the lottery number, the award is £1,000."""

import random

lottery = random.randint(10, 99)
guess = int(input("Enter your two-digit number: "))

l1 = lottery // 10
l2 = lottery % 10

g1 = guess // 10
g2 = guess % 10

if guess == lottery:
    print(f"You have won £10,000! The lottery number was {lottery}")
elif g1 == l2 and g2 == l1:
    print(f"You have won £3,000! The lottery number was {lottery}")
elif g1 in (l1, l2) or g2 in (l1, 2):
    print(f"You have won £1,000! The lottery number was {lottery}")
else:
    print(f"You have not won. The lottery number was {lottery}")