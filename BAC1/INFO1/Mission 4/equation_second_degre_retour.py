"""from math import*
def rho(a,b,c):
    delta=(b**2)-(4*a*c)
    return delta

def n_solutions(a,b,c):
    if rho(a,b,c)>0:
        return 2
    elif rho(a,b,c)==0:
        return 1
    elif rho(a,b,c)<0:
        return 0
 
def solveur(liste):
    for i in liste:
        a=liste[0]
        b=liste[1]
        c=liste[2]
    if n_solutions(a,b,c)==2:
        sol1=(-b-(sqrt(rho(a,b,c))))/(2*a)
        sol2=(-b+(sqrt(rho(a,b,c))))/(2*a)
        if sol1<sol2:
            return [sol1,sol2]
        return [sol2,sol1]
    elif n_solutions(a,b,c)==1:
        return [(-b)/(2*a)]
    elif n_solutions(a,b,c)==0:
        return []
        
print(solveur([4,4,1]))"""

#Qui fonction sur inginious

def solveur(lst):
    ListOfSolutions=[]
    if len(lst)==0:
        return ListOfSolutions
    for i in lst:
        ListOfSolutions.append(solution(i[0],i[1],i[2])) #prend les elements dans a,b,c pour chaque sous liste de la liste solver 
    return ListOfSolutions
























