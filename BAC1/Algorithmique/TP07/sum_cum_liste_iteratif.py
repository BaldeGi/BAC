from max_liste_iteratif import List

def cum_sum(l):
    """
    Calcule la liste des sommes cumulées des éléments de `l`
    par itération
    pre: -
    post: retourne une liste dont le `i`^ième élément est la somme
        des `i` premiers éléments de `l`
    """
    liste=[]
    cm=List()
    if l.is_empty():
        return cm
    liste.append(l.head())
    i=0
    while not l.tail().is_empty():
        l=l.tail()
        liste.append(l.head() + liste[i])
        i+=1
    for i in range(-1,-len(liste)-1,-1):
        cm=cm.concat(liste[i])
    return cm


#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)

print(cum_sum(l))
        