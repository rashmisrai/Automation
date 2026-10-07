# Inheritance in Python

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        return "Meow!"
# Creating instances of Dog and Cat
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", breed="Siamese")


# Inheritance in Python

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def action(self):
        print(f"{self.name} is {self.age} years old")


class Person(Human):
    def actions(self):
        print(f"{self.name} loves playing football at {self.age}")


obj = Person("Rashmi", 24)
obj.action()
obj.actions()

# Super()

Namee = input("Enter name: ")
Salaryy = int(input("Enter salary: "))
Fieldd = input("Enter Field: ")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class HumanBeing(Employee):
    def __init__(self, name, salary, Field):
        super().__init__(name, salary)
        self.Field = Field

    def YOE(self):
        print(f"{self.name} is earning {self.salary} in the field of {self.Field}")


obj1 = HumanBeing(Namee, Salaryy, Fieldd)
obj1.YOE()
