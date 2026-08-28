# Day 1 — Python Fundamentals for AI/ML

## Goal

Learn the basic Python concepts that are required before working with
data and machine learning.

Today's concepts:

1. Variables
2. Lists
3. Dictionaries
4. Loops
5. Conditions
6. Functions
7. Basic data processing

---

# 1. Variables

A variable is used to store a value.

Example:

```python
name = "Shafi"
age = 25
score = 90
```

# 2. Basic Data Types

Common Python data types:

```python
name = "Shafi"       # String
age = 25             # Integer
score = 90.5         # Float
is_student = True    # Boolean


We can check the type using type():

print(type(name))
print(type(age))
print(type(score))
print(type(is_student))

```

# 3. Lists

A list stores multiple values.

Example:

```python

scores = [80, 90, 70, 95, 85]

Python uses zero-based indexing.

Index:    0   1   2   3   4
Value:   80  90  70  95  85

Access values:

print(scores[0])
print(scores[3])

Output:

80
95


## Useful list operations

scores = [80, 90, 70, 95, 85]

print(len(scores))
print(sum(scores))
print(max(scores))
print(min(scores))

len() → number of elements

sum() → total of elements

max() → largest value

min() → smallest value

```

# 4. Dictionaries

A dictionary stores data using key-value pairs.

Example:

```python

student = {
    "name": "Shafi",
    "age": 25,
    "score": 90
}

Access values:

print(student["name"])
print(student["score"])

Output:

Shafi
90

Change a value:

student["score"] = 95

Add a new value:

student["city"] = "Bangalore"

```

# 5. Loops

A loop allows us to process multiple values.

Example:

```python

scores = [80, 90, 70, 95, 85]

for score in scores:
    print(score)

The loop processes each value one by one.

Conceptually:

score = 80
score = 90
score = 70
score = 95
score = 85

```

Loops are very important in AI/ML because we frequently process
large amounts of data.


# 6. Conditions

Conditions allow us to make decisions.

Example:

```python

score = 85

if score >= 80:
    print("Good")
else:
    print("Needs improvement")

Output:

Good

```

# 7. Loop + Condition

We can combine loops and conditions.

```python

scores = [80, 90, 70, 95, 85]

for score in scores:
    if score >= 80:
        print(score)

Output:

80
90
95
85

Only values greater than or equal to 80 are printed.

```

# 8. Functions

A function is a reusable block of code.

Example:

```python

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

Call the function:

scores = [80, 90, 70, 95, 85]

average = calculate_average(scores)

print(average)

Output:

84.0

```

Functions are useful because we can reuse the same logic.