class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def display(self):
        print(self.name, "-", self.score)

    def is_passed(self):
        return self.score >= 50


class GraduateStudent(Student):
    def __init__(self, name, score, university):
        super().__init__(name, score)
        self.university = university

    def research(self):
        print(self.name, "is doing research")