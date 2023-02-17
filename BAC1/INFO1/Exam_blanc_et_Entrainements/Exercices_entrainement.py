def sommes_sous_ensemble(l,n):
    """
    pre: l est une liste(potentiellement vide) d'entiers et n un entier,
    post: Retourne True si l co,tie,t un sous ensembles de valerurs dont la somme
    est egale à n et False sinon(la somme d'un sous ensemble vide peut être considerer
    comme 0)
    """
    for i in range(len(l)):
        if l[i]==n:
            return True
        for j in range(1,len(l)):
            if i!=j:
                if l[i]+l[j]==n:
                    return True
            for k in range(2,len(l)):
                if (i!=j and i!=k) and (j!=k ):
                    if l[i]+l[j]+l[k]==n:
                        return True
    return False

def compte_valid(s):
    s=s.strip(" ")
    chffr=""
    diviseurs=s[-2:]
    for i in range(len(s)):
        if s[i]!="-" and s[i]!=" ":
            if s[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
                return False
    for i in range(1,11):
        if s[i]!="-" and s[i]!=" ":
            chffr+=s[i]
    if int(chffr)%97==int(diviseurs):
        return True
    else:
        return False


def verifier_fichier(filename):
    with open(filename,"r") as file:
        liste=file.read().split("\n")
        for i in liste:
            if not compte_valid(i):
                return False
        return True
    
def caracteres_occurences(l):
    d={}
    lst=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
             if  l[i][j] not in lst:
                 lst.append(l[i][j])
    for k in lst:
        value=[]
        for i in range(len(l)):
            for j in range(len(l[i])):
                if k==l[i][j]:
                    value.append(i)
                    break
        d[k]=value
    return d

def carre_magique(carre):
    l=[]
    ligne=len(carre)
    col=len(carre[0])
    val=sum(carre[0])
    if ligne==col:
        #Pour les lignes
        for i in range(ligne):
            somme=0
            for j in range(col):
                somme+=carre[i][j]
            if somme!=val:#Condition permettant d'arreter l'execution si une ligne n'est pas egale a val(somme de la 1ere ligne)
                return False
            else:
                l.append(somme)
        #Pour les colonnes:
        i,j=0,0
        for i in range(ligne):
            somme=0
            for j in range(col):
                somme+=carre[i][j]
            if somme!=val:#Condition permettant d'arreter l'execution si une colonne n'est pas egale a val(somme de la 1ere ligne)
                return False
            else:
                l.append(somme)
        #Pour les diagonales
        j=-1
        somme,sommes=0,0
        for i in range(ligne):
            somme+=carre[i][i]
            sommes+=carre[i][j]
            j+=-1
        if somme!=val or sommes!=val:#Condition permettant d'arreter l'execution si une diagonale n'est pas egale a val(somme de la 1ere ligne)
            return False
        else:
            l.append(somme)
            l.append(sommes)
        
        #Verifier que toutes les valeurs sont les mêmes
        for i in range(len(l)-1):
            if l[i]!=l[i+1]:
                return False
        return True
    else:
        return False



if __name__ == '__main__':
    print("---- Sommme des Entiers ----")
    print((sommes_sous_ensemble([3,4,7,9,11,12],10)))
    print()
    print("---- Comptes Valides ----")
    print(compte_valid("  068-2492526-41  "))
    print(compte_valid("  012-3456777-83  "))
    print(compte_valid("  012-3456777-27  blabla"))
    print(compte_valid("  012-3456777-27  "))
    print(compte_valid("068-2492527-42  "))
    print()
    print("----Verifier Fichier----")
    
    print()
    print("----Caracteres Occurences----")
    print(caracteres_occurences(["ceci n'est pas une pipe", "le fils de l'homme", "golconda"]))
    print()
    print("----Carre Magique----")
    print(carre_magique([[1,2],[2,1]]))
    print(carre_magique([[12,7,6],[9,5,1],[4,3,8]]))
    print(carre_magique([[2,7,6],[9,5,1],[4,3,8]]))
    print(carre_magique([[8,11,14,1],[13,2,7,12],[3,16,9,6],[10,5,4,15]]))
    print(carre_magique([[11,24,7,20,3],[4,12,25,8,16],[17,5,13,21,9],[10,18,1,14,22],[23,6,19,2,15]]))
    
    
     
    



