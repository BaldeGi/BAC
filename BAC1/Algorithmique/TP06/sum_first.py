def sum_first(t, n):
    """
    Calcule la somme des `n` premiers éléments de `t` avec une boucle
    pre: `t` un tableau (list) non vide
    pre: `n` un entier tel que 1<=`n`<=len(`t`)
    post: retourne la somme des `n` premiers éléments de `t`
    """
    res=0
    for i in range(n):
        res+=t[i]
    return res



print(sum_first([1,2,3,5,7,9,11], 2))