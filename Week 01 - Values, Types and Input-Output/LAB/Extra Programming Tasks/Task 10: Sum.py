"""## Task 10: Sum of First n Integers
Ask for a positive integer `n` and compute the sum `n*(n+1)//2`. Print the result.

**Example Output:**
```
Sum of 1..10 = 55
```"""
n = int(input("Enter a positive integer: "))
sum = n * (n + 1) // 2

print(f"Sum of {n} x ({n} + 1) // 2 = {sum}")