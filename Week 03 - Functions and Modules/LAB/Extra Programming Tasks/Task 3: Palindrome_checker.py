"""
## Task 3: Palindrome Checker
Write a function to check if a given string is a palindrome (reads the same backward as forward).

Some palindrome words are: civic, radar, level, rotor, kayak, madam, refer, rotator, deified, racecar and reviver.

The function should take one string, and return `True` if it is a palindrome, otherwise `False`.
"""

def is_palindrome(check):
    return check == check[: : -1]

for word in ["civic", "lima", "radar"]:
    print(word, is_palindrome(word))
