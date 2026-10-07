# Dictionaries in Python

# Creating a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values in a dictionary
print("Name:", my_dict["name"])  # Output: Name: John
print("Age:", my_dict["age"])    # Output: Age: 30
print("City:", my_dict["city"])  # Output: City: New York

# Adding a new key-value pair to the dictionary
my_dict["country"] = "USA"
print("Updated Dictionary:", my_dict)

# Output: Updated Dictionary: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
my_dict["city"] = "Los Angeles"  # Updating the value of an existing key
print("Updated Dictionary:", my_dict)  # Output: Updated Dictionary: {'name': 'John', 'age': 30, 'city': 'Los Angeles', 'country': 'USA'}

# Removing a key-value pair from the dictionary
del my_dict["age"]
print("Updated Dictionary after deletion:", my_dict)  # Output: Updated Dictionary after deletion: {'name': 'John', 'city': 'Los Angeles', 'country': 'USA'}

# Iterating through a dictionary
for key, value in my_dict.items():
    print(key, ":", value)

#Copying a dictionary
my_dict_copy = my_dict.copy()
print("Copied Dictionary:", my_dict_copy)  # Output: Copied Dictionary: {'name': 'John', 'city': 'Los Angeles', 'country': 'USA'}
