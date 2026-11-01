"""
## Task 10: Pentagon Area
Ask for the side length `s` and compute the area: `area = 5*s**2 / (4*tan(pi/5))`. Print to 2 d.p.

**Example Output:**
```
Area = 172.05
```
*Optional hint:* `from math import tan, pi`
"""
from math import tan, pi

side = float(input("Enter the side length of the pentagon: "))
area = 5 * side ** 2 / (4 * tan(pi / 5))

print(f"Area = {area:.2f}")