def recherche(m,v):
    l=[]
    for i in range(len(m)):
        for j in range(len(m[i])):
          l.append(m[i][j])
          print(l)
    for i in l:
        if v==i:
            return True
    return False
    
print(recherche([[1,2,34],[12,3,10]],3))