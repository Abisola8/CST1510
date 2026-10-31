"""## Task 12: Reverse Number Pattern
Write a program that uses a for loop to print the following reverse number pattern.

```
Expected output:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
```"""

for i in range(5, 0, -1):
    for a in range(i, 0, -1):
        print(a, end=" ")
    print()