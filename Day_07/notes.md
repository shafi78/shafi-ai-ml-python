# Day 7 — Error Handling & Debugging

## Goal

Learn how to handle unexpected situations and debug Python programs.

Today's concepts:

1. Exceptions
2. try
3. except
4. else
5. finally
6. Specific exceptions
7. raise
8. Debugging

---

# 1. Exceptions

An exception occurs when something goes wrong while a program is running.

Example:

```python
number = 10
result = number / 0

This causes:

ZeroDivisionError

```

# 2. try and except

try contains code that might cause an exception.

except handles the exception.

```python

try:
    number = int("hello")
except ValueError:
    print("Invalid number")

```

# 3. Common Exceptions


## ValueError

```python

Occurs when a value is invalid.

int("abc")
TypeError

Occurs when incompatible types are used.

"10" + 5

```

## ZeroDivisionError

```python

Occurs when dividing by zero.

10 / 0

```

## FileNotFoundError

```python

Occurs when trying to open a file that does not exist.

open("missing.txt")

```

## KeyError

```python

Occurs when accessing a missing dictionary key.

student = {"name": "Shafi"}

student["score"]

```

## IndexError

```python

Occurs when accessing an invalid list index.

numbers = [10, 20, 30]

numbers[10]

```

# 4. Multiple except Blocks

Different exceptions can be handled separately.

```python

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")

```

# 5. else

else runs only when no exception occurs.

```python

try:
    number = int("10")

except ValueError:
    print("Invalid number")

else:
    print("Conversion successful")

```

# 6. finally

finally runs whether an exception occurs or not.

```python

try:
    number = int("10")

except ValueError:
    print("Invalid number")

finally:
    print("Program finished")

finally is commonly used for cleanup operations.

```

# 7. raise

raise allows us to create an exception ourselves.

```python

score = -10

if score < 0:
    raise ValueError("Score cannot be negative")

This is useful for validating data.

```

# 8. Functions + Error Handling

Functions can validate their input.

```python

def calculate_average(scores):

    if len(scores) == 0:
        raise ValueError("Scores cannot be empty")

    return sum(scores) / len(scores)

The function can then be called inside try/except.

```

# 9. Error Handling vs Debugging

Error handling asks:

"What should the program do when something goes wrong?"

Debugging asks:

"Why did the program go wrong?"

Debugging steps:

```python

Read the error message.
Check the file and line number.
Inspect the surrounding code.
Check the values and data types.
Fix the underlying problem.

Useful debugging statements:

print(value)
print(type(value))

```