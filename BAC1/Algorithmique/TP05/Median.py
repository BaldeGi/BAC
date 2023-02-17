def median(values):
    """
    pre: `values` est un tableau (list) d objets comparables
    post: renvoie la mesure médiane du tableau `values` sans changer l'ordre du tableau
    """
    def insertion_sort(values):
        """
        pre: `values` est un tableau (list) d objets comparables
        post: renvoie un tableau trié par ordre croissant
        """
        for i in range(len(values)):
            key = values[i]
            j = i - 1
            while j>=0 and values[j] > key:
                values[j+1] = values[j]
                j-=1
            values[j+1] = key
        return values
    #Que ça sur inginious
    lst_trie = insertion_sort(values)
    if len(lst_trie)%2 == 0:
        med = sum(lst_trie[(len(lst_trie)//2)-1:(len(lst_trie)//2)+1])/2
    else:
        med = lst_trie[len(lst_trie)//2]
    return lst_trie , med 
    



print(median([4,1,0,8,5]))
print(median([3,4,1,0,8,5]))



