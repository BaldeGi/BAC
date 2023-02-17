from math import*
#1
def rho(a,b,c):
    delta=(b**2)-(4*a*c)
    return delta
print(rho(1,1,-2))

def n_solutions(a,b,c):
    if rho(a,b,c)>0:
        return 2
    elif rho(a,b,c)==0:
        return 1
    elif rho(a,b,c)<0:
        return 0
print(n_solutions(1,1,-2))
    
def solution(a,b,c):
    if rho(a,b,c)>0:
        sol1=(-b-(sqrt(rho(a,b,c))))/(2*a)
        sol2=(-b+(sqrt(rho(a,b,c))))/(2*a)
        if sol1<sol2:
            return sol1
        return sol2
    elif rho(a,b,c)==0:
        return (-b)/(2*a)
print(solution(1,1,-2))

print("\n")

#2
def rho(a,b,c):
   return (b**2)-(4*a*c)
print(rho(1,1,-2))

def n_solutions(a,b,c):
    if rho(a,b,c)>0:return 2
    elif rho(a,b,c)== 0 : return 1
    else: return 0
print(n_solutions(1,1,-2))

def solution(a,b,c):
    if n_solutions(a,b,c)==2:
        return min((-b+sqrt(rho(a,b,c)))/(2*a) ,(-b-sqrt(rho(a,b,c)))/(2*a))
    elif n_solutions(a,b,c)==1: return (-b)/(2*a)
print(solution(1,1,-2))







        
    
