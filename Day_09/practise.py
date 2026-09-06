# Exercise 1 — Create a Class

# Create:

# class Student:
#     pass

# Create two objects:

# Shafi
# Guru

# Print their types using:

# type(student1)


class Student:
    pass 

Shafi = Student()
Guru = Student()

print(type(Shafi))
print(type(Guru))




# Exercise 2 — Constructor

# Create:

# class Student:
#     def __init__(self, name, score):
#         # your code

# Create:

# Shafi → 85
# Guru → 72

# Print:

# Shafi 85
# Guru 72


class Student:
    def __init__(self,name,score):
        self.name = name 
        self.score = score 

student1 = Student("Shafi",85)
student2 = Student("Guru",95)

print(student1.name, student1.score)
print(student2.name, student2.score)




# Exercise 3 — Method

# Add:

# display()

# Example:

# student.display()

# Expected:

# Shafi - 85


class Student:
    def __init__(self,name,score):
        self.name = name 
        self.score = score 

    def display(self):
        print(self.name,"-",self.score)

student1 = Student("Shafi",85)
student2 = Student("Guru",95)

student1.display()





# Exercise 4 — is_passed()

# Add:

# is_passed()

# Return:

# True

# if score >= 50.

# Test:

# Shafi → 85
# Sam → 45

# Expected:

# Shafi: True
# Sam: False



class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(self.name, "-", self.score)

    def is_passed(self):
        return self.score >= 50


student1 = Student("Shafi", 85)
student2 = Student("Sam", 45)

print(student1.name + ":", student1.is_passed())
print(student2.name + ":", student2.is_passed())






# Exercise 5 — Inheritance

# Create:

# class Student:
#     ...
    
# class GraduateStudent(Student):
#     ...

# Give GraduateStudent a method:

# research()

# Expected:

# Shafi is doing research



class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class GraduateStudent(Student):
    def research(self):
        print(self.name, "is doing research")


student = GraduateStudent("Shafi", 85)

student.research()






# Exercise 6 — super()

# Create:

# class Student:
#     def __init__(self, name, score):
#         ...

# Then:

# class GraduateStudent(Student):
#     def __init__(self, name, score, university):
#         ...

# Use:

# super().__init__(name, score)

# and add:

# self.university = university

# Then print:

# Name: Shafi
# Score: 85
# University: ABC University



class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class GraduateStudent(Student):
    def __init__(self, name, score, university):
        super().__init__(name, score)
        self.university = university


student = GraduateStudent("Shafi", 85, "ABC University")

print("Name:", student.name)
print("Score:", student.score)
print("University:", student.university)