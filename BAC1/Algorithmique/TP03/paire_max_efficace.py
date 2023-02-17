def paire_max_efficace(a):
    """
    Calcule la somme maximale d'une paire d'entiers de `a`
    pre: `a` est un tableau (list) d'entiers
    pre: len(`a`) >= 2
    post: retourne la somme maximale obtenue Ã  partir d'une
        paire d'entiers de `a`
    """
    current_max = max(a)
    l=list(a)
    l[l.index(current_max)]=min(l)
    val=l[0]
    for i in range(len(l)):
        if l[i] > val:
            val = l[i]
    return val + current_max
        
    


#Exemples de test:
print(paire_max_efficace([-1, -5, -4, -5, -9]))
print(paire_max_efficace([8, -4, 6, -6, -1, -6, -7]))
print(paire_max_efficace([0,1]))
print(paire_max_efficace([1,4,9,0,-100,2,-12,40]))
