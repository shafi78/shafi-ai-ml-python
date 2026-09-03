# Exercise 1 — Create a Module

# Create:

# calculator.py

# Add:

# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b

# Then create:

# main.py

# Import the module and print:

# 30
# 10

# using:

# 20 + 10
# 20 - 10




# Exercise 2 — Specific Import

# Using the same calculator.py, import only add.

# Use:

# from calculator import add

# Then:

# print(add(50, 25))

# Expected:

# 75




# Exercise 3 — Built-in Module

# Use:

# import math

# Calculate the square root of:

# 144

# Expected:

# 12.0









# Exercise 4 — Random

# Use:

# import random

# Generate a random number between:

# 1 and 100









# Exercise 5 — __name__

# Create:

# greeting.py

# with:

# def greet(name):
#     return f"Hello {name}"


# if __name__ == "__main__":
#     print(greet("Shafi"))

# Then create:

# main.py

# and import greeting.

# Test what happens when:

# python greeting.py

# versus:

# python main.py

# Pay attention to which print() executes.