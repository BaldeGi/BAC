def plus_fort_reste(n_sieges, resultat_vote):
    '''
    Calcul la repartition des sieges selon la methode du plus
    fort reste (variante du quotient de Hare)
    pre: `n_sieges` > 0
    pre: len(`resultat_vote`) > 1
    pre: `resultat_vote[i]` >= 0
        pour tout `i` tel que 0 <= `i` < len(`resultat_vote`)
    post: retourne un tableau `t` de même longueur que `resultat_vote`
        et tel que `t[i]` est le nombre de sieges attribues au parti
        correspondant a `resultat_vote[i]`
    '''
    nbr_sieges,reste,reste_trie,rslt_v,rest=[],[],[],[],[]
    if len(resultat_vote)==1:
        return [n_sieges]
    for i in range(len(resultat_vote)):
        nbr_sieges.append(0)
    div=sum(resultat_vote)/n_sieges
    for i in range(len(resultat_vote)):
        rslt_v.append(resultat_vote[i]/div)
        nbr_sieges[i]=int(rslt_v[i])
        r=rslt_v[i]-int(rslt_v[i])
        reste.append(r)
    sieges_restant=n_sieges-sum(nbr_sieges)
    for i in reste:
        reste_trie.append(i)
        rest.append(i)
    reste_trie=sorted(reste_trie,reverse=True)
    for j in range(len(reste_trie)):
        if sieges_restant>0:
            for k in range(len(reste)):
                nbr_sieges[reste.index(max(reste))]+=1
                reste[reste.index(max(reste))]=-max(reste)
                sieges_restant-=1
                break
        else:
            return nbr_sieges
                
   
                         


print(plus_fort_reste(5,  [437,478,85]))
print(plus_fort_reste(19,[399, 250, 478, 411, 318, 191, 317, 465, 170, 484, 160, 508, 397, 351, 472, 536, 264]))
print(plus_fort_reste(13,  [482]))
print(plus_fort_reste(20,[308, 121, 194, 121, 436, 98]))
#print(rslt_v[9],rslt_v[10])
#print(reste_trie[8],reste_trie[9])

