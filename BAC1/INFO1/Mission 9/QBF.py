class Item :

    def __init__(self,author,title,serial):
        """
        Méthode d'initialisation.
        @pre  author et title sont des valeurs de type String
              serial est un entier > 0
        @post Une instance de la classe est créée, et représente un objet ayant
              comme auteur author, comme titre title et comme numéro de série serial
        """
        self.__author = author
        self.__title = title
        self.__serial = serial
        

    def __str__(self):
        """
        Méthode de conversion en string.
        @pre  -
        @post le string retourné contient une représentation de cet objet sous la
              forme: [num série] Auteur, Titre
        """
        return "[{}] {}, {}".format(self.__serial,self.__author,self.__title)
    
class CD(Item):
    serial=100000 
    def __init__(self,author,titel,duree):
        super().__init__(author,titel,CD.serial)
        self.duree=duree
        CD.serial+=1
        
    def __str__(self):
        return "{} ({} s)".format(super().__str__(),self.duree)
    
    
item = Item("Radiohead","The Bends",100000)
print(item)
print()
cd = CD("Radiohead","The Bends",2917)
print(cd)
cds = CD("Radiohead","The Bends",2917)
print(cds)
cdss = CD("Radiohead","The Bends",2917)
print(cdss)

