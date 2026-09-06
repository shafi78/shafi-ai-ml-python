from student import Student, GraduateStudent


students = [
    Student("Shafi", 85),
    Student("Guru", 72),
    Student("Cindrella", 91),
    Student("Sam", 45)
]


print("Student Report")
print("==============")
print()

total_score = 0
passed_count = 0


for student in students:
    student.display()
    print("Passed:", student.is_passed())
    print()

    total_score += student.score

    if student.is_passed():
        passed_count += 1


average_score = total_score / len(students)

print("Average Score:", average_score)

print()
print("Graduate Student")
print("================")

graduate = GraduateStudent("Shafi", 85, "ABC University")

print("Name:", graduate.name)
print("Score:", graduate.score)
print("University:", graduate.university)

graduate.research()

print()
print("Total Passed:", passed_count)