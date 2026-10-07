# Sets in Python

# A set is a collection which is unordered, unchangeable*, and unindexed.

roll_nos = {101, 102, 103, 104, 105}
print(roll_nos)

roll_nos.add(106)
print(roll_nos)

roll_nos.update([107,108,109,110])
print(roll_nos)

nos = [111,112,113,114,115]
roll_nos.update(nos)
print(roll_nos)

roll_nos.discard(110)
print(roll_nos)

'''
roll_nos.clear()
print(roll_nos)
'''
roll_nos.remove(111)
print(roll_nos)

stud_nos = {101,103,105,107,109}
print(roll_nos.intersection(stud_nos))
print(roll_nos & stud_nos)
print(roll_nos.difference(stud_nos))

print(roll_nos.union(stud_nos))
print(roll_nos | stud_nos)

print(roll_nos.symmetric_difference(stud_nos)) # means elements in either roll_nos or stud_nos but not in both
