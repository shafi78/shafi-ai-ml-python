# Exercise 1 — Tuple

numbers = (10, 20, 30, 40, 50)

# Print:

# first element
# last element
# length

# Then try:

# numbers[0] = 100

# Observe what happens.

print(numbers[0])
print(numbers[-1])
print(len(numbers))



# Exercise 2 — Set

# Given:

# numbers = [10, 20, 10, 30, 20, 40, 30, 50]

# Create a set containing only unique numbers.

# Expected conceptually:

# {10, 20, 30, 40, 50}

numbers = {10,20,10,30,20,40,30,50}

print(numbers)


# or

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = set(numbers)

print(unique_numbers)




# Exercise 3 — enumerate()

# Given:

students = ["Rahul", "Amit", "Priya", "Neha"]

# Print:

# 1. Rahul
# 2. Amit
# 3. Priya
# 4. Neha

# Use enumerate().

for index,student in enumerate(students,start=1):
    print(index,student)



# Exercise 4 — zip()

# Given:

names = ["Rahul", "Amit", "Priya"]
scores = [85, 72, 91]

# Print:

# Rahul - 85
# Amit - 72
# Priya - 91

# Use zip().

for name , score in zip(names,scores):
    print(name,score)



# Exercise 5 — Sorting

# Given:

scores = [45, 91, 67, 88, 72, 95]

# Create:

# Ascending:
# [45, 67, 72, 88, 91, 95]

# Descending:
# [95, 91, 88, 72, 67, 45]

# Use sorted().

sorted_scores_ascending = sorted(scores)
sorted_scores_descending = sorted(scores, reverse=True)

print(sorted_scores_ascending)
print(sorted_scores_descending)



# Exercise 6 — Sort Students

# Given:

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91},
    {"name": "Neha", "score": 45},
    {"name": "Arjun", "score": 67}
]

# Sort them by score from highest to lowest.

# Expected:

# Priya - 91
# Rahul - 85
# Amit - 72
# Arjun - 67
# Neha - 45


sorted_students = sorted(
    students,
    key=lambda student:student['score'],
    reverse=True
)

print(sorted_students)