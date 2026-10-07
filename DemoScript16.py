# Method overriding

class Parent:
    def greet(self):
        print("Hello, I am the parent.")

class Child(Parent):
    def greet(self):
        print("Hello, I am the child.")

obj = Child()
obj.greet()  # Output: Hello, I am the child.

# Method overriding - allows a subclass to provide a specific implementation of a method that is already defined in its parent class.