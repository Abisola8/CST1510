"""
## Task 11: Square Root Table
Use the `math.sqrt` function. Write a program that prints the following table using the `sqrt` function in the `math` module.

```
Number      Square root
0   	 	0.00
2    		1.41
4    		2.00
6    		2.45
8    		2.83
10    		3.16
12    		3.46
14    		3.74
16    		4.00
18    		4.24
```
"""

import math

print("Number\t\tSquare root")
for i in range(0, 20, 2):
    print(f"{i}\t\t{math.sqrt(i):.2f}")
    