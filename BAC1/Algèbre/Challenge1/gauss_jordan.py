def gauss(m):
    for i in range(len(m)-1):
        if m[i][i]==0:
            line = m[i]
            m[i] = m[i+1]
            m[i+1] = line
            if m[i+1][i]!=0:
                for j in range(len(m)-1):
                    if i<j and m[i][i]!=0:
                        pivot= m[j][i]/ m[i][i]
                        for k in range(len(m[i])):
                            m[j][k]-= pivot*m[i][k]
        else:
            for j in range(len(m)-1):
                 if i<j and m[i][i]!=0:
                    pivot= m[j][i]/ m[i][i]
                    for k in range(len(m[i])):
                        m[j][k]-= pivot*m[i][k]
                
    for i in range(len(m)-1):
        if m[i][i]==0:
            line = m[i]
            m[i+1] = line
            m[i] = m[i+1]
            for j in range(len(m)-1):
                 if i<j and m[i][i]!=0:
                    pivot= m[j][i]/ m[i][i]
                    for k in range(len(m[i])):
                        m[j][k]-= pivot*m[i][k]
        else:
            for j in range(len(m)-1):
                if i<j and m[j][j]!=0:
                    pivot= m[i][j]/ m[j][j]
                    for k in range(len(m[i])):
                        if j < j+1:
                            m[i][k]-= pivot*m[j][k]
                            
                            
                            
    
    for i in range(len(m)-1):
        if m[i][i]!=0:
            div=m[i][i]
            for j in range(len(m[i])):
                m[i][j]/=div
            
    for i in m:
        print(i)


print(gauss([[1,1,2],
             [2,1,1],
             [3,1,1],
             [4,3,1]
            ]))

print(gauss([[-2,2,-3],
             [-3,1,1]
            ]))


print(gauss([[1,2],
             [2,1]
            ]))   
    
    
    
    
"""
for i in range(len(m)):
        if m[i][i]==0:
            line = m[i]
            m[i] = m[i+1]
            m[i+1] = line
            if m[i+1][i]!=0:
                for j in range(len(m)):
                    if i<j and m[i][i]!=0:
                        pivot= m[j][i]/ m[i][i]
                        for k in range(len(m[i])):
                            m[j][k]-= pivot*m[i][k]
        else:
            for j in range(len(m)):
                 if i<j and m[i][i]!=0:
                    pivot= m[j][i]/ m[i][i]
                    for k in range(len(m[i])):
                        m[j][k]-= pivot*m[i][k]
                
    for i in range(len(m)):
        if m[i][i]==0:
            line = m[i]
            m[i+1] = line
            m[i] = m[i+1]
            for j in range(len(m)):
                 if i<j and m[i][i]!=0:
                    pivot= m[j][i]/ m[i][i]
                    for k in range(len(m[i])):
                        m[j][k]-= pivot*m[i][k]
        else:
            for j in range(len(m)):
                if i<j and m[j][j]!=0:
                    pivot= m[i][j]/ m[j][j]
                    for k in range(len(m[i])):
                        if j < j+1:
                            m[i][k]-= pivot*m[j][k]
                            
                            
                            
    
    for i in range(len(m)):
        if m[i][i]!=0:
            div=m[i][i]
            for j in range(len(m[i])):
                m[i][j]/=div
            
    for i in m:
        print(i)"""
      
    
