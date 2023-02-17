def proximity(tuple1,tuple2,theta_1,theta_2):
    if absolute(tuple1[0],tuple2[0])<=theta_1 and euclidian_distance(tuple1[1],tuple2[1])<theta_2:
        return True
    else:
        return False
def croisement(tra1,tra2,theta_1,theta_2):
    for i in tra1:
        for j in tra2:
            if proximity(i,j,theta_1,theta_2)==True:
                return True
    return False

def matrix_for_traces(l,theta_1,theta_2):
    matrix=[]
    for i in range(len(l)):
        liste=[]
        for j in range(len(l)):
            if croisement(l[i],l[j],theta_1,theta_2)==True:
                liste.append(1)
            else:
                liste.append(0)
        matrix.append(liste)
    return matrix
#Fonction qui ne marche que sur inginious car il y'a des fonctions deja implementer