# Operators in Python

# 1. Arithmetic Operators
num1 = 10
num2 = 5
print(num1+num2)

print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)
print(num1**num2)

# 2. Assignment Operators

data1 = 30
data1 += 5  # data1 = data1 + 5
print(data1)
data1 -=5  # data1 = data1 - 5
print(data1)
data1 *= 2  # data1 = data1 * 2
print(data1)
data1 /= 3  # data1 = data1 / 3
print(data1)
data1 %= 4  # data1 = data1 % 4
print(data1)
data1 //= 5
# data1 = data1 // 5
print(data1)

# 3. Logical Operators : and, or, not
a = True
b = False
print(a and b)
print(a or b)
print(not a)

# 4. Comparison Operators : ==, !=, >, <, >=, <=
x = 10
y = 20
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# 5. Bitwise Operators : &, |, ^, ~, <<, >>
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print(p & q)  # Bitwise AND
print(p | q)  # Bitwise OR
print(p ^ q)  # Bitwise XOR
print(~p)     # Bitwise NOT
print(p << 1) # Left shift
print(p >> 1) # Right shift

# 6. Membership Operators : in, not in
list1 = [1, 2, 3, 4, 5]
print(3 in list1)
print(6 not in list1)

# 7. Identity Operators : is, is not
str1 = "Hello"
str2 = "Hello"
print(str1 is str2)
print(str1 is not str2)