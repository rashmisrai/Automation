# Functions in python

def login(username, password):
    if username == "Rashmi" and password == '1234':
        return "Login successful"
    else:
        return "Login failed"

logged_in = login("Rashmi", "1234")
print(logged_in)

# Functions with default parameters
def greet(name="Guest"):
    return f"Hello, {name}"

greeting = greet()
print(greeting)
greeting = greet("Rashmi")
print(greeting)

# args and kwargs
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info("Rashmi", 25, city="New York", country="USA")

# Sum of numbers using *args
def addition(*nums):
    total = 0
    for n in nums:
        total += n
    return total

result = addition(1, 2, 3, 4)
print("Sum:", result)

result = addition(1, 2, 3, 4, 5)
print("Sum:", result)

empName = "Rashmi"

def name():
    print("Employee name is:", empName)

name()

# Scope of variable

age = 25
print("Age:", age)

def show_age():
    global age
    age = 30
    print("Age inside function:", age)


show_age()
print("Age outside function:", age)


