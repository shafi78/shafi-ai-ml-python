# Day 4 — Python Data Utilities

## Goal

Learn useful Python tools for working with collections of data.

Today's concepts:

1. Tuples
2. Sets
3. enumerate()
4. zip()
5. sorted()
6. lambda

---

# 1. Tuples

A tuple is similar to a list, but it cannot be modified after creation.

```python
scores = (85, 90, 72)

Access elements:

print(scores[0])

Tuples are immutable.

This is not allowed:

scores[0] = 100

Tuples are also commonly used when returning multiple values from
a function.

def analyze(numbers):
    return 10, 20, 30

The returned value is:

(10, 20, 30)

```

# 2. Sets

A set stores unique values.

```python

numbers = {10, 20, 30, 20, 10}

print(numbers)

Duplicate values are removed.

Sets are useful when we need unique values.

Example:

names = ["Rahul", "Amit", "Rahul", "Priya", "Amit"]

unique_names = set(names)

print(unique_names)

```

A set should mainly be used for uniqueness and membership checking.

# 3. enumerate()

enumerate() allows us to get both the index and the value while
looping.

```python

students = ["Rahul", "Amit", "Priya"]

for index, student in enumerate(students):
    print(index, student)

Output:

0 Rahul
1 Amit
2 Priya

We can start the index from another number:

for index, student in enumerate(students, start=1):
    print(index, student)

Output:

1 Rahul
2 Amit
3 Priya

```

# 4. zip()

zip() combines corresponding elements from multiple collections.

```python

names = ["Rahul", "Amit", "Priya"]
scores = [85, 72, 91]

for name, score in zip(names, scores):
    print(name, score)

Output:

Rahul 85
Amit 72
Priya 91

```

zip() is useful when we have related data stored in separate lists.

# 5. sorted()

sorted() creates a sorted version of a collection.

```python

scores = [85, 72, 91, 45, 67]

sorted_scores = sorted(scores)

print(sorted_scores)

Output:

[45, 67, 72, 85, 91]

For descending order:

sorted_scores = sorted(scores, reverse=True)

Output:

[91, 85, 72, 67, 45]

```

# 6. Sorting Dictionaries

We can sort a list of dictionaries using a key.

```python

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91}
]

Sort by score:

sorted_students = sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

```

This sorts students by their score from highest to lowest.

# 7. lambda

A lambda is a small anonymous function.

```python

Normal function:

def get_score(student):
    return student["score"]

Equivalent lambda:

lambda student: student["score"]

It can be used as the key for sorting:

sorted(
    students,
    key=lambda student: student["score"],
    reverse=True
)

```

This means:

"Sort students using their score."