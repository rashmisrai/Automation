# Tuples in Python

# A tuple is a collection which is ordered and unchangeable.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[2:5]) # returns the items from index 2 to 4
print(fruits[::2])  # returns every second item in the tuple
print(fruits[::-1])  # returns the items in reverse order
print(fruits[::-2])  # returns every second item in the tuple in reverse order

new_fruits = list(fruits)
print(new_fruits)

new_fruits.insert(7, "banana")
print(new_fruits)

fruits = tuple(new_fruits)
print(fruits)