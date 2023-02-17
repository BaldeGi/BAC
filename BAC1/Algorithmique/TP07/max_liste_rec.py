from max_liste_iteratif import List

def maximum_rec(l):
    def maximum_recs(l, current_max=None):
        """
        Calcule le maximum d une liste par récursion
        pre: `l` contient au moins un élément
        post: retourne l élément maximum de `l`
        """

        if l.tail().is_empty():
            if current_max == None:
                return l.head()
            elif l.head() > current_max:
                return l.head()
            return current_max
        else:
            if not current_max is None:
                if l.tail().head()>l.head():
                    if l.tail().head()> current_max:
                        current_max = l.tail().head()
                else:
                    if l.head()> current_max:
                        current_max = l.head()
            else:
                current_max  = l.head()
        return  maximum_recs(l.tail(),current_max)
    return maximum_recs(l)




#Exemple de test:
l = List()
l = l.concat(50)
l = l.concat(4)
l = l.concat(30)
l = l.concat(2)
l = l.concat(100)
print(maximum_rec(l))





