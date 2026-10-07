# If, if-else, elif, nested if in python

# Example of if statement
a = 10
if a > 5:
    print("a is greater than 5")

# Example of if-else statement
b = 3
if b > 5:
    print("b is greater than 5")
else:
    print("b is not greater than 5")

# Example of if-elif-else statement
c = 7
if c > 10:
    print("c is greater than 10")
elif c > 5:
    print("c is greater than 5 but less than or equal to 10")
else:
    print("c is less than or equal to 5")

# Example of nested if statement
d = 15
if d > 10:
    print("d is greater than 10")
    if d > 20:
        print("d is also greater than 20")
    else:
        print("d is not greater than 20")