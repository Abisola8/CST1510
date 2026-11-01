"""
## Task 3: Rectangle Class

Create a class `Rectangle` with `width` and `height` and methods `area()` and `perimeter()`.
Create a list of 4 rectangles and print the area and perimeter of each, then print which rectangle has the largest area.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = float(width)
        self.height = float(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self. width * 2) + (self.height * 2)

r1 = Rectangle(3, 4)
r2 = Rectangle(5, 3)
r3 = Rectangle(8, 4)
r4 = Rectangle(5, 10)

print(r1.area(), r1.perimeter())
print(r2.area(), r2.perimeter())
print(r3.area(), r3.perimeter())
print(r4.area(), r4.perimeter())

largest_area = max(r1.area(), r2.area(), r3.area(), r4.area())

print(f"The largest rectangle area is {largest_area}")