def sum_first_rec(t, n):
    """
    Calcule la somme des `n` premiers éléments de `t` par récursion
    pre: `t` un tableau (list) non vide
    pre: `n` un entier tel que 1<=`n`<=len(`t`)
    post: retourne la somme des `n` premiers éléments de `t`
    """
    if n==1:
        return t[n-1]
    return t[n-1] + sum_first_rec(t[:n],n-1)
    
    
    
    
    
print(sum_first_rec([1,2,3,5,7,9,11], 4))
    
    
