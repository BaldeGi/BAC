def paire_max(a): #Approche par force brute
    """
    Calcule la somme maximale d'une paire d'entiers de `a`
    pre: `a` est un tableau (list) d'entiers
    pre: len(`a`) >= 2
    post: retourne la somme maximale obtenue Ã  partir d'une
        paire d'entiers de `a`
    """
    somme_maximale=-1000000000000000
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            somme_courante = a[i] + a[j]
            if somme_courante > somme_maximale:
                somme_maximale = somme_courante
    return somme_maximale

print(paire_max([-1, -5, -4, -5, -9]))
print(paire_max([8, -4, 6, -6, -1, -6, -7]))
print(paire_max([0,1]))
print(paire_max([1,4,9,0,-100,2,-12,40]))
