# Day 9 — Classes, Objects & Inheritance

## 1. OOP

OOP stands for Object-Oriented Programming.

It organizes related data and behavior together.

## 2. Class

A class is a blueprint/template for creating objects.

Example:

```python

class Student:
    pass

```

## 3. Object

An object is an instance of a class.

Example:

```python

student = Student()

```

## 4. Constructor

__init__() initializes an object when it is created.

Example:

```python

def __init__(self, name, score):
    self.name = name
    self.score = score

```

## 5. self

self refers to the current object.

self.name means the name belonging to that object.

## 6. Attributes

Attributes are data stored inside an object.

Example:

```python

self.name
self.score

```

## 7. Methods

Methods are functions defined inside a class.

Example:

```python

def is_passed(self):
    return self.score >= 50

```

## 8. Why Use Classes

Without classes, related data is scattered across separate
variables, which gets messy with many records.

Classes group data + behavior into a single, reusable object.

Example:

```python

student1 = Student("Shafi", 85)
student2 = Student("Guru", 72)

```

## 9. Inheritance

Inheritance allows a child class to reuse functionality
from a parent class.

Example:

```python

class GraduateStudent(Student):
    pass

```

## 10. super()

super() allows a child class to call functionality
from the parent class.

Example:

```python

super().__init__(name, score)

```

## 11. AI/ML Connection

OOP is heavily used in Python libraries and ML frameworks.

Models, datasets, optimizers, and other components
are commonly represented as objects.

Example:

```python

class Model:

    def __init__(self, name):
        self.name = name

    def train(self):
        print("Training model")

    def predict(self):
        print("Making prediction")

```