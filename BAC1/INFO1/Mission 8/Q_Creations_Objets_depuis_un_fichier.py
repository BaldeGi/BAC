class Student:
    def __init__(self, firstname, surname, mark):
        ''' crée une instance de Student où firstname et surname sont des str et mark un int
        '''
        self.firstname = firstname
        self.surname = surname
        self.mark = mark
        
    def  marks_from_file(self,filename):
        liste=[]
        with open("fichier.txt") as file:
           l=file.readlines()
           for i in range(len(l)):
               l[i]=l[i].strip("\n").split(" ")
               liste.append(Student(l[i][0],l[i][1],int(l[i][2])))
           return liste



stu=Student("Balde","Lamarana",11)
print(stu.marks_from_file("fichier.txt"))
        
        
    