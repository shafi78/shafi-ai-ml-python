# Student Ranking Analyzer

students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91},
    {"name": "Neha", "score": 45},
    {"name": "Arjun", "score": 67}
]

# Your program should output:

# Student Ranking Analyzer

# 1. Priya - 91
# 2. Rahul - 85
# 3. Amit - 72
# 4. Arjun - 67
# 5. Neha - 45

# Highest Score: 91
# Lowest Score: 45

# Passed Students:
# Priya
# Rahul
# Amit
# Arjun


def rank_students(students):
    return sorted(
        students,
        key=lambda student: student["score"],
        reverse=True
    )


def get_passed_students(students):
    return [
        student for student in students
        if student["score"] >= 50
    ]


def get_highest_score(students):
    return max(student["score"] for student in students)


def get_lowest_score(students):
    return min(student["score"] for student in students)

ranked_students = rank_students(students)

print("Student Ranking Analyzer")
print()


for rank, student in enumerate(ranked_students, start=1):
    print(rank, ".", student["name"], "-", student["score"])


highest_score = get_highest_score(students)
lowest_score = get_lowest_score(students)

print()
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)

passed_students = get_passed_students(ranked_students)

print()
print("Passed Students:")

for student in passed_students:
    print(student["name"])