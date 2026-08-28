# Exercise 1

# Print numbers from 1 to 10 using range().

# Expected:

# 1
# 2
# 3
# ...
# 10

for i in range(1,11):
    print(i)



# Exercise 2

# Print only even numbers from 1 to 20.

# Expected:

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

for i in range(2,22,2):
    print(i)



# Exercise 3

# Given:

numbers = [10, 20, 30, 40, 50, 60, 70]

# Using slicing, create:

# [20, 30, 40]

# Then:

# [40, 50, 60, 70]


print(numbers[1:4])
print(numbers[3:7])



# Exercise 4

# Given:

numbers = [1, 2, 3, 4, 5]

# Create:

# [1, 4, 9, 16, 25]

# Use list comprehension.

squares = [number * number for number in numbers]

print(squares)



# Exercise 5

# Given:

numbers = [10, 15, 20, 25, 30, 35, 40]

# Create a new list containing only numbers greater than 25.

# Expected:

# [30, 35, 40]

ans = [number for number in numbers if number > 25]
print(ans)



# Exercise 6

# Given:

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91},
    {"name": "Neha", "score": 45},
    {"name": "Arjun", "score": 67}
]

# We want a new list containing only students who passed.

# Passing means:

# score >= 50


passed_students = [
    student for student in students
    if student["score"] >= 50
]

print(passed_students)