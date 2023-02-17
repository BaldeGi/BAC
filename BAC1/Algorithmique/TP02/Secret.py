def secret(n):
    '''
    pre: `n` > 0
    post: ???
    '''
    r=1
    for i in range(n,0,-1):
        temp=i
        for j in range(i,0,-1):
            temp+=temp
        r=max(r,temp)
    return r
        
        
print(secret(3))


def secret(n):
    '''
    pre: `n` > 0
    post: ???
    '''
    r=1
    for i in range(1,n+1):
        r=i*2**i
    return r
        
               
print(secret(3))

def secret(n):
    '''
    pre: `n` > 0
    post: ???
    '''
    return n*2**n
    
print(secret(3))
    