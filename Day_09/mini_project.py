# Day 9 Mini Project — Student Management System

# This project will combine:

# Classes
# Objects
# __init__()
# self
# Attributes
# Methods
# Inheritance
# super()
# Lists of objects
# Basic data processing


# We'll keep the Student classes in student.py and the actual program in main.py.

# 1. student.py

# Create a Student class.

# Each student should have:

# name
# score

# The class should have:

# display()

# Print:

# Shafi - 85
# is_passed()

# Return:

# True

# if score is >= 50.

# Otherwise:

# False

# Then create a child class:

# GraduateStudent

# which inherits from Student.

# It should additionally have:

# university

# and a method:

# research()

# which prints:

# Shafi is doing research

# 2. main.py

# Create several students:

# Shafi → 85
# Guru → 72
# Cindrella → 91
# Sam → 45

# Also create a graduate student:

# Shafi → 85 → ABC University

# Use your classes to:

# Display each student's information.
# Check whether each student passed.
# Display the graduate student's university.
# Call research().
# Count how many students passed.
# Calculate the average score.

# Expected Output

# Something similar to:

# Student Report
# ==============

# Shafi - 85
# Passed: True

# Guru - 72
# Passed: True

# Cindrella - 91
# Passed: True

# Sam - 45
# Passed: False

# Average Score: 73.25

# Graduate Student
# ================

# Name: Shafi
# Score: 85
# University: ABC University
# Shafi is doing research

# Total Passed: 3