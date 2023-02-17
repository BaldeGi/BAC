def max_interval(mesures):
    '''
    Etant donne une sequence de mesures espacees de 10 minutes,
    determine l'intervalle d'une heure durant lequel le niveau d'eau est le plus eleve en moyenne.

    pre: - mesures est un tableau (list)
         - len(mesures) >= 7
    post: renvoie l'indice du tableau mesures auquel commence le premier sous-tableau de longueur 7 de plus forte moyenne.
    '''
    indice=0
    moyenne=sum(mesures[:7])/len(mesures[:7])
    for i in range(len(mesures)):
        if i+7<=len(mesures):
            liste=mesures[i:i+7]
            m=sum(liste)/len(liste)
            if m>moyenne:
                moyenne=m
                indice=i
        else:
            return indice
    
print(max_interval( [48, 26, 2, 16, 32, 31, 25, 50, 19, 30]))
print(max_interval(  [10, 0, 5, 10, 30, 10, 20, 30]))