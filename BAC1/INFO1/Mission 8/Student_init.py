class Student:
    def __init__(self,name,surname,birth_date,email):
         # À implémenter
        self.name=name
        self.surname=surname
        self.birth_date=birth_date
        self.email=email

stu=Student("Balde","Lamarana","2000","lbalde")
print(stu.name)