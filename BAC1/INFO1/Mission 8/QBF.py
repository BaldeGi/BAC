class Employe:
    
    def __init__(self,nom,salaire):
        self.nom=nom
        self.salaire=salaire
        
    def augmente(self,pourcentage):
        self.salaire+=self.salaire*(pourcentage/100)
    
        
    def __str__(self):
        return "{} : {}".format(self.nom,self.salaire)
    
    
    
    
    
    
charles = Employe("Charles", 2500)
charles.augmente(10)
print(charles)