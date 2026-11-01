"""
## Task 5: Count Range
Python's standard library includes a method named `count` that determines how many times a specific value occurs in a list.
In this exercise, you will create a new function named `countRange` which determines and returns the number of elements within a list that are greater than or equal to some minimum value and less than some maximum value.

Your function will take three parameters: the list, the minimum value and the maximum value. It will return an integer result.

Include a main program that demonstrates your function for several different lists, minimum values and maximum values.
Ensure that your program works correctly for both lists of integers and lists of floating-point numbers.
"""
def countRange(list, min_val, max_val):
    count = 0
    for value in list:
        if value >= min_val and value < max_val:
            count += 1
    return count

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]

print(countRange(list_1, 3, 7))
print(countRange(list_2, 2.5, 8.0))