def is_adn(text):
    """
    pre: 's' est une chaine caractère
    post: retourne True si la chaîne de caractères
    contient uniquement les caractères a, t, c ou g
    (à la fois en majuscules et en minuscules)
    et False sinon
    """
    adn=["a","t","c","g"]
    for i in text:
        if i!=i.lower():
            i=i.lower()
        if i not in adn:
            return False
    return True
                
            
def positions(text,car):
    """
    pre: 's' et 'p' sont deux chaines de caractères
    post: retourne les positions des occurences de 'p' dans 's'
    """
    text,car=text.lower(),car.lower()
    i,j=0,1
    index=[]
    while j <len(text):
        if text[i:i+len(car)]==car:
            index.append(i)
        j+=1
        i+=1
    return index

                
def distance_h(text1,text2):
    """
    pre:'s' et 'p' sont deux chaines de caractères
    post: retourne la distance 'Hamming' entre les
    deux chaines.
    """
    dist=0
    text1,text2=text1.upper(),text2.upper()
    for i in range(len(text1)):
        if text1[i]!=text2[i]:
            dist+=1
    return dist
        
def distances_matrice(l):
    """
    pre: 'l' est une liste qui contient des chaines
    de caractères.
    post: retourne la distance (le nombre de positions
    où les deux chaines diffèrent) dans une matrice entre toutes les chaines.
    """
    matrix=[]
    for i in range(len(l)):
        matrix.append([])
        for j in range(len(l)):
            if len(l[i])==len(l[j]):
                matrix[i].append(distance_h(l[i],l[j]))
            else:
                matrix[i].append(None)
              
    return matrix




print(is_adn("AcaA"))
print(positions('CbHHbBvbbcF','bBc'))
print(distance_h("ATGAC","TGACG"))
print(distances_matrice(["AG", "AT", "GT", "ACG", "ACT" ]))



