def puiss_rec(x, n):
    """
    Exponentiation rapide par récursion
    pre: `n` >= 0
    post: retourne `x`^`n`
    """
    if n==0:
        return 1
    else:
        if n%2==0:
            return puiss_rec(x*x,n/2)
        else:
            return x*(puiss_rec(x*x ,(n-1)/2))
    
    
print(puiss_rec(2, 64))