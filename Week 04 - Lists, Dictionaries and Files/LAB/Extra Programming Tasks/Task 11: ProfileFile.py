"""
## Task 11: Profile File
Write a program that:
1. Creates a file called `my_profile.txt`
2. Writes 3 lines: your name, your age, and your favorite color
3. Reads the file back and prints each line with a label

**Example output:** "Name: Alex", "Age: 20", "Favorite Color: Blue"
"""

with open("my_profile.txt", "w") as f:
    f.write("Name: Abisola\n")
    f.write("Age: 24\n")
    f.write("Favourite Colour: Blue\n")

with open("my_profile.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.strip())
