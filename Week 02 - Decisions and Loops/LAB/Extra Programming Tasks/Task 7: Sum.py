"""## Task 7: Sum of Numbers from 1 to n
Write a program to accept a number `n` from a user and calculate the sum of all numbers from 1 to a given number n.

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10).

```
Expected output
Enter the value n: 10
The sum of all numbers until 10 is 55
```"""
n = int(input("Enter a number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(f"The sum of all numbers until {n} is {sum}")