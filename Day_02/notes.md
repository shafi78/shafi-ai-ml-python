# Day 2 — Python Data Handling

## Goal

Learn Python features that are useful when processing data:

1. range()
2. List slicing
3. List comprehensions
4. Processing lists of dictionaries

---

# 1. range()

### range(stop)

```python
for i in range(5):
    print(i)

Output:

0
1
2
3
4

The stop value is excluded.

range(start, stop)
for i in range(2, 6):
    print(i)

Output:

2
3
4
5

range(start, stop, step)
for i in range(0, 10, 2):
    print(i)

Output:

0
2
4
6
8

```


# 2. List Slicing

```python
numbers = [10, 20, 30, 40, 50, 60]
numbers[1:4]

Output:

[20, 30, 40]

The syntax is:

list[start:stop]

The stop index is excluded.

Examples:

numbers[:3]
numbers[3:]
numbers[::2]

```


# 3. List Comprehension

A list comprehension provides a short way to create a new list.

Normal loop:

```python
squares = []

for number in numbers:
    squares.append(number * number)

List comprehension:

squares = [number * number for number in numbers]

General structure:

[expression for item in list]
With a condition
result = [number for number in numbers if number > 20]

```

This creates a list containing only numbers greater than 20.


# 4. Lists of Dictionaries

Example:

```python

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91}
]

Loop through the students:

for student in students:
    print(student["name"])

Filter students:

for student in students:
    if student["score"] >= 80:
        print(student["name"])

Using list comprehension:

top_students = [
    student for student in students
    if student["score"] >= 80
]

```


