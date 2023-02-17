def plus_forte_moyenne(n_sieges, resultat_vote):
    '''
    Calcul la repartition des sieges selon la methode de la plus
    forte moyenne (variante de D Hondt)
    pre: `n_sieges` > 0
    pre: len(`resultat_vote`) > 1
    pre: `resultat_vote[i]` >= 0
        pour tout `i` tel que 0 <= `i` < len(`resultat_vote`)
    post: retourne un tableau `t` de meme longueur que `resultat_vote`
        et tel que `t[i]` est le nombre de sieges attribues au parti
        correspondant a `resultat_vote[i]`
    '''
    nbr_sieges,rslt_v,l=[],[],[]
    for i in range(len(resultat_vote)):
        nbr_sieges.append(0)
    for i in range(len(resultat_vote)):
        rslt_v.append(n_sieges*resultat_vote[i]/sum(resultat_vote))
        nbr_sieges[i]=(int(rslt_v[i]))
    sieges_p=sum(nbr_sieges)
    while sieges_p<n_sieges:
        for i in range(len(resultat_vote)):
            l.append(resultat_vote[i])
        for i in range(len(l)):
            l[i]/=(nbr_sieges[i]+1)
        nbr_sieges[l.index(max(l))]+=1
        sieges_p+=1
        l=[]
    return nbr_sieges
        
print(plus_forte_moyenne(11,  [437,478,85]))    
print(plus_forte_moyenne(16,  [200,108,294,424,172,528,74,207,141,488,317,423,86,204,256,477,218,203,262,105,100,337,515,296,292,222,480,458,
                              549,465,225,113]))
print(plus_forte_moyenne(12,  [40,30,20,10]))
print(plus_forte_moyenne(11,  [130,100,70,60,50,10])) 




