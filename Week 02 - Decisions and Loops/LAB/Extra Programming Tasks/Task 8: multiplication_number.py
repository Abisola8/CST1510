"""## Task 8: Multiplication Table of a Number
Write a program to print the multiplication table of a given number.

For example, `num = 2`:

```
Expected output:

0 x 2 = 0
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
4 x 2 = 8
5 x 2 = 10
6 x 2 = 12
7 x 2 = 14
8 x 2 = 16
9 x 2 = 18
```"""

number = int(input("Enter a number: "))

for i in range(10):
    print(f"{i} x {number} = {i * number}")