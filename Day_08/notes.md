# Day 8 — Python Modules & Packages

# 1. What is a Module?

A module is a Python file containing reusable code.

```python

Example:
math_utils.py

```

# 2. Why Modules?

- Code organization
- Code reuse
- Easier maintenance
- Separation of responsibilities

# 3. import

```python

import student_utils

student_utils.calculate_average(scores)

```

# 4. from import

```python

from student_utils import calculate_average

calculate_average(scores)

```

# 5. Module Alias

```python

import student_utils as su

su.calculate_average(scores)

```

# 6. Built-in Modules

```python

Examples:
- math
- random
- datetime
- os

```

# 7. __name__ == "__main__"

Used to ensure certain code runs only when
the Python file itself is executed.

# 8. Package

A package is a collection of related Python modules.

```python

Module → one .py file
Package → collection of modules

```

# 9. AI/ML Connection

Large AI/ML projects use modules and packages
to organize data loading, preprocessing,
training, evaluation, and utilities.