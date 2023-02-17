def moyenne_mobile(lst,n) :        # NE PAS EFFACER CETTE LIGNE
    """
    @pre:  lst est une liste de réels non vide
           n un entier strictement positif : 0 <= n <= len(lst)//2
    @post: retourne une nouvelle liste contenant les moyennes mobiles
           calculées à partir de lst comme défini dans l'énoncé de cette question
           lst n'a pas été modifiée
    """
    res=[]
    for i in range(len(lst)):
        if i<n:
            l=lst[0:i+n+1]
            m=sum(l)/len(l)
            res.append(m)
        else:
            l=lst[i-n:i+n+1]
            m=sum(l)/len(l)
            res.append(m)
    return res
        
            
        

def moyenne_mobile1(lst,n) :        # NE PAS EFFACER CETTE LIGNE
    """
    @pre:  lst est une liste de floats non vide
           n un entier strictement positif : 0 < n <= len(lst)
    @post: retourne une nouvelle liste contenant les moyennes mobiles
           calculées à partir de lst comme défini dans l'énoncé de cette question
           lst n'a pas été modifiée
    """
    res,l=[],[]
    for i in range(len(lst)):
        l.append(lst[i])
        if len(l)<=n:
            m=sum(l)/len(l)
            res.append(m)
        else:
            del l[0]
            m=sum(l)/len(l)
            res.append(m)
    return res
    
if __name__=='__main__':
    print(moyenne_mobile([0,1,2,3],1))                 # [0.5, 1.0, 2.0, 2.5]
    print(moyenne_mobile([0,1,2,3],2))                 # [1.0, 1.5, 1.5, 2.0]
    print()
    print(moyenne_mobile1([0,1,2,3],2))                # [0.0, 0.5, 1.5, 2.5]
    print(moyenne_mobile1([0,1,2,3],3))                # [0.0, 0.5, 1.0, 2.0]
    
