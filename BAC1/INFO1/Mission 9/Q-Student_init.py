class Student:
    noma=1
    def __init__(self,firstname,surname,birthday,email):
        self.firstname=firstname
        self.surname=surname
        self.birthday=birthday
        self.email=email
        self.noma=Student.noma
        Student.noma+=1

    def __str__(self):
        return "L'etudiant numero {}: {} {} né le {}  peut être contacté par {} ".format(self.noma,
        self.firstname, self.surname,self.birthday,self.email)
       



stu = Student('Lamarana', 'Balde', "10 Avril" , 'email.@gmail.com')
tu = Student('Lama', 'Balde', "11 mai" , 'email.@gmail.com')
print(tu.__str__())