"""
## Task 2: Dice Throws
Create a list of seven dice throws.
- The throws should be randomly generated and added to the list.
- Shuffle the list and print it out.
- Sort the list in descending order and print it out.
- Count the occurrences and print them out.
"""

import random

throws = []

for i in range(7):
    throws.append(random.randint(1, 6))

print(f"Original throws: {throws}")
random.shuffle(throws)
print(f"Shuffled throws: {throws}")
print(f"Descending throws: {(sorted(throws)[::-1])}")

for i in range(1, 7):
    print(f"Occurrences: {i} shows {throws.count(i)} times")