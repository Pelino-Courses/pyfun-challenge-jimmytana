"""
here we imported two files student and coursers so that we can be able to vie thier enrollment
"""

from student import Student
from course import Course
class Enrollment(Student, Course):
    def __init__(self, student_id, student_name, student_age, student_sex,course_id, course_name, date):
        Student.__init__(self, student_id, student_name, student_age, student_sex)
        Course.__init__(self, course_id, course_name)
        self.date = date
    def __str__(self):
        return (f"Enrollment Date: {self.date} \nStudent: {self.id}\nCourse: {self.course_name}")
    