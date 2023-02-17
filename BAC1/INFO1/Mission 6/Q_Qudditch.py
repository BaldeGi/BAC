def  referee(score_file):
    point_eq_1,point_eq_2,team=0,0,[]
    with open(score_file,"r") as file:
        l=file.readlines()
    for line in range(len(l)):
        team.append(l[line].strip("\n").split(" "))
    tm1=team[0][0]
    for i in range(2,len(team)):
        if team[i][0]==tm1:
             point_eq_1+=int(team[i][1])
             if int(team[i][1])>=150:
                return team[0][0]
        else:
            point_eq_2+=int(team[i][1])
            if int(team[i][1])>=150:
                return team[1][0]
    if point_eq_1>point_eq_2:
        return team[0][0]
    return team[1][0]
    
print(referee("score.txt"))


#Code pour plus de deux equipe (Général)

def referee(score_file) :
    try:
        with open(score_file,"r") as file:
             l = file.readlines()
    except:
        raise FileNotFoundError
    for i in range(len(l)):
        l[i] = l[i].split()
    for i in l:
        if len(i)==1:
            indice = l.index(i)
    for i in range(indice+1):
        l[i].append(0)
    for j in range(indice+1,len(l)):
        for i in range(indice+1):
            if l[i][0]==l[j][0]:
                l[i][1]+=int(l[j][1])
                if l[i][1]>=150:
                    return l[i][0]
    indice_maximum = l[0][1]
    for i in range(indice+1):
        if l[i][1]>indice_maximum:
            indice_maximum=i
    if l[0][1]!= indice_maximum:
        return l[indice_maximum][0]
    return l[0][0]

print(referee("score.txt"))




        