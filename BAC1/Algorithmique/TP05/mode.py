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


def mode(values):
    """
    pre: `values` est un tableau (list) d objets comparables
    post: renvoie le mode du tableau (ou le mode de plus petite valeur si plusieurs modes)
    """
    lst_trie = insertion_sort(values)
    modes , l = [], []
    for i in lst_trie:
        if i not in l:
            l.append(i)
            modes.append(lst_trie.count(i))
    maximum=max(modes)
    indice_max=[]
    indice_max.append(modes.index(maximum))
    modes[modes.index(maximum)]=-maximum
    for i in range(len(modes)):
        if modes[i]==maximum:
            indice_max.append(i)
    minimum = l[indice_max[0]]
    for i in indice_max:
        if len(indice_max)==1:
            return l[i]
        elif l[i]< minimum:
            minimum = l[i]
    return minimum
            
        
            
        

        
    
    
    
print(mode([2,6, 2, 4, 7, 5, 6])) #2
print(mode([6, 0, 4, 8, 7, 6, 4, 7, 5, 9, 3, 8, 2, 4, 2, 1])) #4
print(mode([1,2,2,3,3,3,4,4,4,4])) #4
print(mode([6, 2, 7, 4, 5, 6]))





