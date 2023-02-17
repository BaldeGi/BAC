
def equal(l, d):
    for key,value in d.items():
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j]!=0 and (i,j)==key:
                    if l[i][j]!=value:
                        return False
                elif l[i][j]!=0 and (i,j) not in d:
                    return False
    return True
    
       
            
    
print(equal([[0, 2, 4], [4, 1, 0]],{(0,1): 2, (0,2): 4, (1,0): 4, (1,1): 1}))