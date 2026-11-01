"""
## Task 2: Dog Class

Create a class `Dog` with `name` and `age`, and two methods:
- `bark()` prints "<name> says Woof!"
- `birthday()` increases the dog's age by 1

Create a dog, call `bark()`, call `birthday()` twice and print the new age.
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1
        print(self.age)

dog = Dog("Jasper", 5)

print(dog.bark())
dog.birthday()
print(dog.birthday())