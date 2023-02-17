class Character:
    def __init__(self,life=100,attack_point=10):
        self.life=life
        self.attack_point=attack_point
        
        
    def attack(self,target):
        target.get_hit(self.attack_point)
        
        
    def get_hit(self,damage):
        self.life-=damage
        
class Cratos(Character):
    def __init__(self,life=100,attack_point=10,experience=0):
        super().__init__(life,attack_point)
        self.experience=experience
        
        
    def gain_XP(self,amount):
        self.experience+=amount
        while self.experience>=10:
            self.experience-=10
            self.attack_point+=1
        
        

class Drauf(Character):
    def __init__(self,life, attack_point):
        super().__init__(life,attack_point)
        
ch=Character()
cra=Cratos()
d=Drauf(100,10)
(cra.gain_XP(50))
print(cra.experience)
print(cra.attack_point)
        