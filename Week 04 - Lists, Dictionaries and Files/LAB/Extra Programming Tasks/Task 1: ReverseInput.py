"""
## Task 1: Reverse Input
Write a program that reads integers from the user and stores them in a list.
Use 0 as a sentinel value to mark the end of the input.
Once all of the values have been read, your program should display them (except for the 0) in reverse order, with one value appearing on each line.
"""

numbers = []

while True:
    number = int(input("Enter an integer (0 to stop): "))
    if number == 0:
        break
    else:
        numbers.append(number)

print(f"The numbers in reverse order are: {numbers[:: -1]}")