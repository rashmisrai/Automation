# Typecasting

a = 100
b = '200'
# print(a + b)  This will raise an error because you cannot add an integer and a string

# To fix this, we need to convert the string to an integer
b = int(b)
print(b + a)

c = 10.5
d = str(c)  # Convert float to string
print(d + " is a float converted to string.")
print(type(d))