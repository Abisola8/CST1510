"""
## Task 3: Sum of a Matrix Row
Write a function that returns the sum of all the elements in a specified row in a matrix using the following header:

```python
def sum_row(matrix, rowIndex):
```

Write a test program that reads a 4-by-4 matrix and displays the sum of each row.
"""
def sum_row(matrix, rowIndex):
    total = 0
    for i in matrix[rowIndex]:
        total += i
    return total

matrix = []

for a in range(4):
    row = input(f"Enter row {a + 1}: ").split()
    matrix.append([float(x) for x in row])

for b in range(4):
    print(f"Sum of row {b}: {sum_row(matrix, b)}")