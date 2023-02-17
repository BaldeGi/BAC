class Cratos:
    def __init__(self,weapon):
        self.weapon=weapon
        
    def set_weapons(self,weapons): # Rajouter s a Weapon pour differencier l'arme du debut et le nouveau
        self.weapons=weapons
        return "Cratos : Yesss!!! Je change ce {} pour prendre cette {}".format(self.weapon,self.weapons) #Rajouter
    
    def hit(self,enemy):
        enemy.get_hit(self.weapon.attack)
    
class Drauf:
    def __init__(self,life):
        self.life=life
        
    def get_hit(self,damage):
        self.life-=damage
        return self.life # Rajouter aussi
        
class Weapon:
    def __init__(self, attack):
        self.attack=attack
        
    def __str__(self,attack): #Fonction qui est Ajouter pour rendre plus marrant
        self.attack-=attack
        return "Cratos: Mince! Il reste {} balle dans la Kalach mais je vais encore la recharger ".format(self.attack)
        
        
cra=Cratos("Pistolet")
print("Cratos: Oh non! L'arme de depart est un petit ",cra.weapon)
print(cra.set_weapons("Kalash")) #Changer son arme

dref=Drauf(30)
print("Drauf : Mon niveau de vie de est ",dref.life,",je suis trop un champion")
print("Drauf : Ohh non! mon niveau de vie après avoir reçu 17 coup de fusil à cause d'une erreur tactique est de {}".format(dref.get_hit(17)))

wep=Weapon(15)
print(wep.__str__(12))


