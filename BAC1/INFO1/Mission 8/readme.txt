class Duree :
    def to_secondes(self) :
    """
    Retourne le nombre total de secondes de cette instance de Duree (self).
    """
    pass

    def delta(self,d) :
    """
    Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
    en secondes (positif si ce temps-ci est plus grand).
    """
    pass 

    def apres(self,d):
    """
    Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
    retourne False sinon.
    """
    pass

   def ajouter(self,d):
   """
   Ajoute une autre Duree d à cette instance de Duree (self).
   Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
   en reportant au besoin les valeurs hors limites sur les unités supérieures
   (60 secondes = 1 minute, 60 minutes = 1 heure).
   """
    pass

   def __str__(self):
    """
    Retourne cette durée sous la forme de texte "heures:minutes:secondes".
    Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
    retourne le String désiré avec les nombres en deux chiffres en ajoutant
    les zéros nécessaires.
    """
    pass
    
class Chanson :
    
    def __str__(self):
    """
    Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
    Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
    """  
    pass

class Album :
    def add(self,chanson):
    """
    la fonction doit retourner False si la longueur de l'Album a atteind 100 chansons ou a depasser 75 minutes si non elle retourne True 
    """
    pass
    def __str__(self):
    """
    doit retourner un album de cette forme:
    Album 21 (12 chansons, 00:47:11)
    01: White_Wedding - Billy_Idol - 00:04:12
    """

Toutes les classes ont fonctionnés d'après nos tests on a eu un peu de souci pour la partie si on lis le fichier de le partager en plusieurs Album differents
mais au finale tous s'est bien passé, on a peu eu le temps pour faire des tests sur cette dernière partie.