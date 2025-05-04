from instructor import Instructor
from student import Student 
class Teaching_Assistant(Instructor, Student):
    def __init__(self,ta_id, ta_name, ta_age, ta_sex, ta_course):
        Student.__init__(ta_id, ta_name, ta_age, ta_sex)
        Instructor.__init__(ta_id, ta_name, ta_age, ta_sex, ta_course)
    def __str__(self):
        return (f"Name: {self.name}")