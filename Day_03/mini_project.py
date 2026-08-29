# Student Data Analyzer

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91},
    {"name": "Neha", "score": 45},
    {"name": "Arjun", "score": 67}
]

# Create these functions:

# print_students()
# calculate_average()
# get_top_student()
# get_passed_students()
# get_failed_students()
# get_high_scorers()

# Your final program should produce:

# Student Data Analyzer

# Students:
# Rahul - 85
# Amit - 72
# Priya - 91
# Neha - 45
# Arjun - 67

# Average Score: 72.0

# Top Student: Priya
# Top Score: 91

# Passed Students:
# Rahul
# Amit
# Priya
# Arjun

# Failed Students:
# Neha

# High Scorers (80+):
# Rahul
# Priya


# print_students()

def print_students(students):
    for student in students:
        print(student["name"], "-", student["score"])

print_students(students)


# calculate_average()

def calculate_average(students):
    total = 0 

    for student in students:
        total += student['score']

    return total/len(students)

average = calculate_average(students)

print("Average Score:", average)


# get_top_student()

def get_top_student(students):
    top_student = students[0]

    for student in students:
        if student["score"] > top_student["score"]:
            top_student = student

    return top_student

top_student = get_top_student(students)

print("Top Student:", top_student["name"])
print("Top Score:", top_student["score"])


# get_passed_students()

def get_passed_students(students):
    return [student for student in students if student['score'] >= 50]

passed_students = get_passed_students(students)

print("Passed Students:")

for student in passed_students:
    print(student["name"])


# get_failed_students()

def get_failed_students(students):
    return [
        student for student in students
        if student["score"] < 50
    ]

failed_students = get_failed_students(students)

for student in failed_students:
    print(student["name"])


# get_high_scorers()

def get_high_scorers(students):
    return [
        student for student in students
        if student["score"] >= 80
    ]

high_scorers = get_high_scorers(students)

for student in high_scorers:
    print(student["name"])