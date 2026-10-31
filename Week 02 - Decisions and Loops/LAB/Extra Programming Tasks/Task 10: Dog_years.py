"""## Task 10: Dog Years
It is commonly said that one human year is equivalent to 7 dog years.
However, this simple conversion fails to recognise that dogs reach adulthood in approximately two years.
As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.

Write a program that implements the conversion from human years to dog years described in the previous paragraph.
Ensure that your program works correctly for conversions of less than two or more human years.
Your program should display an appropriate error message if the user enters a negative number."""

human_years = float(input("Enter the number of human years: "))

if human_years < 0:
    print("Error: Please enter a positive number")
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 2 * 10.5 + (human_years - 2) * 4

print(f"{human_years} human years is = {dog_years} dog years")