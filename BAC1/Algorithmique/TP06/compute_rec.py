def compute_rec(n):
    """
    Approche récursive
    pre: `n` est un entier >= 0
    post: retourne la somme des entiers de 0 à `n` compris
    """
    
    if n==0:
        return 0
    return n + compute_rec(n-1)


print(compute_rec(3))