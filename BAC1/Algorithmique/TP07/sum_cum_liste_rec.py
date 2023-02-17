from max_liste_iteratif import List

def cum_sum_rec(l):
    """
    Calcule la liste des sommes cumulées des éléments de `l`
    par récursion
    pre: -
    post: retourne une liste dont le `i`^ième élément est la somme
        des `i` premiers éléments de `l`
    """
    def cum_sum_aux(l,res):
        if l.is_empty():
            return List()
        r=l.head()+res
        lst=List(r)
        lst.tail_list=cum_sum_aux(l.tail(),res+l.head())
        return lst
    return cum_sum_aux(l,0)
 

#Exemple de test:
l = List()
l = l.concat(5)
l = l.concat(4)
l = l.concat(3)
l = l.concat(2)
l = l.concat(1)
cm = cum_sum_rec(l)
print(cm)
