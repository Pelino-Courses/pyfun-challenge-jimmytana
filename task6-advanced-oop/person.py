class Person:
    def __init__(self,id,name,age,sex):
        self.id=id
        self.name=name
        self.age=age
        self.sex=sex
        if not isinstance(id,int):
            raise ValueError("pleasea id shold be a number integer")
        if not isinstance(name,str):
            raise TypeError("name should be a string")
        if not isinstance(age,int):
            raise ValueError("age should be an integer")
        if not isinstance(sex,str):
            raise TypeError("sex should be string")
        
    def __str__(self):
        print(f"Id: {self.id} \n Nane: {self.name} \n sex: {self.sex}")
    