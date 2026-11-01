"""
## Task 8: Pure Python EDA: Custom Statistics Functions
The **median** is a robust statistic that protects us from outliers, while the **mean** is easily skewed.
Write functions to calculate both.

1. Write a function `get_mean(data)` that takes a list of numbers and returns their average.
2. Write a function `get_median(data)` that takes a list of numbers, sorts them, and returns the middle value. (Assume the list has an odd number of elements for simplicity.)
3. Test your functions on a regular list and a list with a massive outlier to see the difference.

```python
regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]
```
"""
def get_mean(data):
    total = 0
    for value in data:
        total += value
    return total / len(data)

def get_median(data):
    ordered = sorted(data)
    return  ordered[len(ordered) // 2]

regular_data = [40, 42, 45, 48, 50]
outlier_data = [40, 42, 45, 48, 1000]

print(get_mean(regular_data))
print(get_median(regular_data))
print(get_mean(outlier_data))
print(get_mean(outlier_data))