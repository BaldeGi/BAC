class Animal:
    def __init__(self,name,diurnal=None,nb_legs=None,asleep=False):
        self.name=name
        self.diurnal=diurnal
        self.nb_legs=nb_legs
        self.asleep=asleep

    def sleep(self):
        if not self.asleep:
            self.asleep=True
            return self.asleep
        else:
            raise RuntimeError("L'animal dort déjà")

    def wake_up(self):
        if self.asleep:
            self.asleep=False
            return self.asleep
        else:
            raise RuntimeError("L'animal s'est déjà réveillé")



class Lion(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.diurnal=True
        self.nb_legs=4

    def roar(self):
        print("ROARRR!!!")


class Owl(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.diurnal=False
        self.nb_legs=2

    def fly(self):
        pass

class Giraffe(Animal):
    def __init__(self,name,neck_length):
        super().__init__(name)
        self.diurnal=True
        self.nb_legs=4
        self.neck_length=neck_length
        if (type(neck_length) == int or type(neck_length) == float) and neck_length > 0:
            self.neck_length = neck_length
        else:
            raise ValueError
    
class Zoo:
    def __init__(self):
        self.animals=[]

    def add_animal(self,animal):
        if isinstance(animal,Animal):
            self.animals.append(animal)
        else:
            raise ValueError
        
    #Petit programme en plus pour tester les animaux et voir les animaux qui sont dans mon zoo 
    def lst(self):
        l=[]
        for i in self.animals:
            if isinstance(i,Giraffe):
                l.append((i.name,i.neck_length))
            else:
                l.append(i.name)
        return l

#Cette fonction create_my_zoo() fait partie de ce qui nous a été demandé d'implementer sur inginious
def create_my_zoo():
    zoo = Zoo()
    zoo.add_animal(Lion("Gérard"))
    zoo.add_animal(Owl("Pétunia"))
    zoo.add_animal(Giraffe("Melmann",1))
    zoo.add_animal(Giraffe("Cyrano",2.5))
    return zoo

if __name__ == "__main__":
    print(create_my_zoo())
    print()
    
    zoo = Zoo()
    zoo.add_animal(Lion("Gérard"))
    zoo.add_animal(Owl("Pétunia"))
    zoo.add_animal(Giraffe("Melmann",1))
    zoo.add_animal(Giraffe("Cyrano",2.5))
    print(zoo.lst())
    
    
    
    
    
