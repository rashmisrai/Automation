# For loop in python

fruits =   ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit: " + fruit)

marks = [85, 90, 78, 92, 88]
total_marks = 0
for mark in marks:
    total_marks += mark
average_marks = total_marks / len(marks)
print("Average Marks:", average_marks)  # Output: Average Marks: 86.6

names = ("John", "Alice", "Bob")
for name in names:
    print("Name: " + name)

# Dictionary iteration
student_scores = {
    "John": 85,
    "Alice": 90,
    "Bob": 78
}
for student, score in student_scores.items():
    print(student + "'s score: " + str(score))



# While loop

a = 1
while a < 10:
    print("a is:", a)
    a += 1

# If we don't give a condition in while loop it will run infinite times

# do while loop is not available in python but we can use while loop to achieve the same functionality

#Example of do while loop in python
b = 1
while True:
    print("b is:", b)
    b += 1
    if b > 5:
        break

