from max_liste_iteratif import List

def length(l):
    """
    Calcule la taille d une liste à l aide d une boucle
    pre: -
    post: retourne la taille de la liste `l`
    """
    def longueur(l,res=1):
        if l.is_empty():
            return 0
        if l.tail().is_empty():
            return 1
        while not l.tail().is_empty():
            l=l.tail()
            res+=1
        return res
    return longueur(l)
        
            



#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(30)
l = l.concat(2)
l = l.concat(1)

print(length(l))