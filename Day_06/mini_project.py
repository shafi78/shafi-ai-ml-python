# students.txt

# Create this file:

# Shafi,85
# Guru,72
# Cindrella,91
# Sam,45
# Alex,67

# Your Python program should:

# 1. Read the file

# Use:

# with open(...)
# 2. Convert each line into data

# For example:

# Shafi,85

# should become something like:

# {"name": "Shafi", "score": 85}

# Hint:

# line.split(",")
# 3. Create a list of students

# You should end up with:

# [
#     {"name": "Shafi", "score": 85},
#     {"name": "Guru", "score": 72},
#     {"name": "Cindrella", "score": 91},
#     {"name": "Sam", "score": 45},
#     {"name": "Alex", "score": 67}
# ]
# 4. Calculate

# Your program should find:

# Average Score: 72.0
# Highest Score: 91
# Lowest Score: 45
# 5. Find passing students

# Passing:

# score >= 50

# Expected:

# Shafi
# Guru
# Cindrella
# Alex
# 6. Generate report.txt

# Your Python program should create report.txt.

# It should contain:

# Student Report

# Shafi - 85
# Guru - 72
# Cindrella - 91
# Sam - 45
# Alex - 67

# Average Score: 72.0
# Highest Score: 91
# Lowest Score: 45

# Passed Students:
# Shafi
# Guru
# Cindrella
# Alex


students = []

with open("./Day_06/students.txt", "r") as file:

    for line in file:
        name,score = line.strip().split(",")

        student = {
            "name": name,
            "score": int(score)
        }

        students.append(student)


# 3. Calculate scores

scores = [student["score"] for student in students]

average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)


# 4. Find passing students

passed_students = [
    student["name"]
    for student in students
    if student["score"] >= 50
]


# 5. Print results

print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)

print("\nPassed Students:")
for name in passed_students:
    print(name)



# 6. Generate report.txt
with open("./Day_06/report.txt", "w") as file:

    file.write("Student Report\n\n")

    for student in students:
        file.write(f"{student['name']} - {student['score']}\n")

    file.write(f"\nAverage Score: {average}\n")
    file.write(f"Highest Score: {highest}\n")
    file.write(f"Lowest Score: {lowest}\n")

    file.write("\nPassed Students:\n")

    for name in passed_students:
        file.write(f"{name}\n")