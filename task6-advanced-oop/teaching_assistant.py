from instructor import Instructor
from student import Student 
"""
we need to import instructor and student as teaching assistance are being consided as student too
"""
class Teaching_Assistant(Instructor, Student):
    def __init__(self,ta_id, ta_name, ta_age, ta_sex, ta_course):
        Student.__init__(ta_id, ta_name, ta_age, ta_sex)
        Instructor.__init__(ta_id, ta_name, ta_age, ta_sex, ta_course)
    def __str__(self):
        return (f"Name: {self.name}")