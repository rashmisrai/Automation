# Lists in python

fruits = ["Apple", "Grapes", "Banana", "Orange", "Mango"]
print(fruits)

flowers = ["Rose", "Lily", "Tulip", "Daisy"]
print(flowers)

print(len(flowers))
print(len(fruits))

print(fruits[0])
print(flowers[1])

print(fruits[0:4])
print(flowers[2:4])

fruits.insert(2, "Pineapple")
print(fruits)

flowers.insert(0, "Sunflower")
print(flowers)

fruits.append("Kiwifruit")
print(fruits)

flowers.append("Marigold")
print(flowers)

fruits.remove("Banana")
print(fruits)

flowers.remove("Marigold")
print(flowers)

fruits.pop(2)
print(fruits)

flowers.pop(2)
print(flowers)

fruits.reverse()
print(fruits)

flowers.reverse()
print(flowers)

fruits.sort()
print(fruits)

flowers.sort(reverse=True)
print(flowers)

fruit_basket = fruits.copy()
print(fruit_basket)

if "Mango" in fruits:
    print("Mango is present in the fruits list.")
else:
    print("Mango is not present in the fruits list.")

if "Lily" in flowers:
    print("Lily is present in the flowers list.")
else:
    print("Lily is not present in the flowers list.")