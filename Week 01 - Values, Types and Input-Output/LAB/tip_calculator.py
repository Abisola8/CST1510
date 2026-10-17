"""
## Tip Calculator

**Uses:** `input()`, `float()`/`int()`, arithmetic, f-string formatting

A bill was $150.00, split between 5 people, with a 12% tip. Each person
should pay `(150.00 / 5) * 1.12 = 33.6`, formatted to 2 decimal places:
`33.60`.

1. Ask for the total bill.
2. Ask for how many people are splitting it.
3. Ask for the tip percentage (as a whole number, e.g. `12` for 12%).
4. Calculate what each person owes and print it formatted to exactly 2
   decimal places.
"""

total = int(input("What is the total bill? "))
people = int(input("How many people are splitting the bill? "))
tip_percent = int(input("What is the tip percentage? "))

each_person = (total / people) * (1 + tip_percent / 100)

print(f"Each person's bill is: {each_person:.2f}")