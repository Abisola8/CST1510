""" ## Task 1: Student Class

Create a class `Student` with attributes `name` and `age` set in `__init__`.
Create two student objects and print their attributes using dot notation.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

s1 = Student("Abisola", 24)
s2 = Student("Josh", 20)

print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)