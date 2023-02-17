def mystere(n):
    '''
    pre: `n` > 0
    post: ???
    '''
    r=0
    for i in range(n+1):
        for j in range(1,i+1):
            for k in range(j, i+j+1):
                r=r+1
    return r


print(mystere(3))
print(mystere(4))

#OU

def mystere(n):
    '''
    pre: `n` > 0
    post: ???
    '''
    return (((n)*(n+1)*(2*n+1))/6) + ((n)*(n+1)/2) #Formule somme(i^2+i)
print(mystere(3))
print(mystere(4))
