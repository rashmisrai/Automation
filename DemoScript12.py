# Classes and objects in python
class Demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_age(self):
        print("Age is:", self.age)

p1 = Demo("Rashmi", 25)
print(p1.name)
print(p1.age)
p1.show_age()



