# Constructors in python are special methods that are automatically called when an object of a class is created.
# They are used to initialize the attributes of the class. The constructor method in Python is defined using the `__init__` method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

Human = Person("Alice", 30)
Human.show_info()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print(f"Name is {self.name} and Age is {self.age}")


person = Person("Rashmi", 24)
person.details()
