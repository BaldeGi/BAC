def top3(mesures):
    '''
    Etant donne une sequence de mesures espacees de 10 minutes, identifie les trois mesures les plus élevées.

    pre: - mesures est un tableau (list)
         - len(mesures) >= 3
    post: renvoie un tableau t de longueur 3 tel que mesures[t[i]] correspond à la i^eme mesure la plus elevee.
    Si plusieurs mesures identiques sont raportées, les indices de ses mesures sont ordonnés.
    '''
    m,l=[],[]
    for i in mesures:
        m.append(i)
    for i in range(3):
        l.append(m.index(max(m)))
        m[m.index(max(m))]=m[m.index(min(m))]-1 #ou min(m)-1
    return l

        
                
            
    
    
    

print(top3([47, 3, -45]))
print(top3([0, 1, 2, 3]))
print(top3([0, 2, 2, 3]))


#if not top3([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0,1,2]:
    #print("Top 3 au début")

#if not top3([0, 1, 2, 3]) == [3,2,1]:
    #print("Top 3 à la fin")