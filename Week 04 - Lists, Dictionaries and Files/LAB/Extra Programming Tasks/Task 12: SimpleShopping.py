"""
## Task 12: Simple Shopping List
Create a program that:
1. Writes a shopping list to `shopping.txt` (5 items, one per line)
2. Reads the file and prints "You need to buy: [item]" for each item
3. Counts and displays the total number of items
"""

with open("shopping.txt", "w") as f:
    f.write("Bananas\n")
    f.write("Apples\n")
    f.write("Oranges\n")
    f.write("Toothpaste\n")
    f.write("Salad\n")

with open("shopping.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(f"You need to buy: {line.strip()}")

print(f"Total items: {len(lines)}")