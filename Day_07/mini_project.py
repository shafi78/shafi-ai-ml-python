# Safe Student Data Analyzer

# 1. Create students.txt

# Put this inside:

# Shafi,85
# Guru,72
# Cindrella,91
# Sam,45
# Alex,67
# John,abc

# Notice:

# John,abc

# This is intentionally invalid.

# 2. Your task

# Create mini_project.py.

# Step 1 — Read the file

# Use:

# with open("students.txt", "r") as file:
# Step 2 — Process each line

# For every line:

# Shafi,85

# split it into:

# name = "Shafi"
# score = "85"

# Then convert:

# score = int(score)
# Step 3 — Handle invalid scores

# When Python reaches:

# John,abc

# this will fail:

# int("abc")

# Handle the ValueError.

# Print:

# Invalid score for John

# Important: Don't stop the program. Continue processing the other students.

# 4. Store valid students

# Create dictionaries like:

# {
#     "name": "Shafi",
#     "score": 85
# }

# Store them in a list.

# Expected valid students:

# Shafi
# Guru
# Cindrella
# Sam
# Alex

# John should not be included.

# 5. Calculate statistics

# Calculate:

# Average score

# Expected:

# Average: 72.0
# Highest score

# Expected:

# Highest: 91
# Lowest score

# Expected:

# Lowest: 45
# 6. Find passed students

# Passing score:

# >= 50

# Expected:

# Passed students:
# Shafi
# Guru
# Cindrella
# Alex

# Sam failed because:

# 45 < 50
# 🎯 Expected output

# Your program should produce something roughly like:

# Invalid score for John

# Average: 72.0
# Highest: 91
# Lowest: 45

# Passed students:
# Shafi
# Guru
# Cindrella
# Alex




def parse_student(line):
    name, score = line.strip().split(",")

    try:
        score = int(score)
    except ValueError:
        raise ValueError(f"Invalid score for {name}")

    return {
        "name": name,
        "score": score
    }


students = []

try:
    with open("./Day_07/students.txt", "r") as file:

        for line in file:
            try:
                student = parse_student(line)
                students.append(student)

            except ValueError as e:
                print(e)

except FileNotFoundError:
    print("File not found")
    exit()


# Calculate average
total = 0

for student in students:
    total += student["score"]

average = total / len(students)


# Find highest and lowest
highest = students[0]["score"]
lowest = students[0]["score"]

for student in students:
    if student["score"] > highest:
        highest = student["score"]

    if student["score"] < lowest:
        lowest = student["score"]


# Find passed students
passed_students = []

for student in students:
    if student["score"] >= 50:
        passed_students.append(student)


# Print results
print()
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)

print()
print("Passed students:")

for student in passed_students:
    print(student["name"])