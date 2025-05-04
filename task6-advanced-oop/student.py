from person import Person
class Student(Person):
    def __init__(self,student_id:int, student_name:str, student_age:int, student_sex:str):
        super().__init__(student_id, student_name, student_age, student_sex)
    def __str__(self):
        return (f"StudentId: {self.id} \n Name: {self.name}")
    