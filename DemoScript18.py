import Methods

class Child:
    def greet(self):
        print("Hello, I am the child.")

obj  = Methods.Parent()
obj.greet()  # Output: Hello, I am the parent.

child_obj = Child()
child_obj.greet()  # Output: Hello, I am the child.