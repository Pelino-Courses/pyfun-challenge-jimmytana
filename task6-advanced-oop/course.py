from student import Student
class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []
    def __str__(self):
        return (f"Course: {self.course_name}")
    def add_student(self, student:Student):
        self.students.append(student)
    
    
    def __iter__(self):
        
        for student in self.students:
            if isinstance(student, Student):
                yield student
        
    def show_students(self):
        print(f"Students enrolled in {self.course_name}")
        for student in self:
            print(student)