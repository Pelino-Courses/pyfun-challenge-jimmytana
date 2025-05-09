"""
as instructor is a person too we do need to import person
"""

from person import Person
class Instructor(Person):
    def __init__(self, id, name, age, sex, instructor_course):
        super().__init__(id, name, age, sex)
        self.instructor_course = instructor_course
    def __str__(self):
        return (f"Instructor: {self.name}\n Course: {self.instructor_course}")
    