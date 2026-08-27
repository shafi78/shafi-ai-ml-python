# Student Performance Analyzer

# Rahul - 85
# Amit - 72
# Priya - 91
# Neha - 45
# Arjun - 67

# Average Score: 72.0

# Top Student: Priya
# Top Score: 91

# Passed: 4
# Failed: 1

# Students with 80+:
# Rahul - 85
# Priya - 91


students = [
    {"name": "Rahul", "score": 85},
    {"name": "Amit", "score": 72},
    {"name": "Priya", "score": 91},
    {"name": "Neha", "score": 45},
    {"name": "Arjun", "score": 67}
]

tot = 0
top_student = students[0]
passed = 0
failed = 0

for stud in students:
    print(stud['name'],"-",stud['score'])

    tot += stud['score']

    if stud["score"] > top_student["score"]:
        top_student = stud

    if stud['score'] >= 50:
        passed += 1
    else:
        failed += 1


print("Average Score: ",tot/len(students))
print("Top Student:", top_student["name"])
print("Top Score:", top_student["score"])

print("Passed:", passed)
print("Failed:", failed)

print("Students with 80+:")

for stud in students:
    if stud['score'] >= 80:
        print(stud['name'],"-",stud["score"])