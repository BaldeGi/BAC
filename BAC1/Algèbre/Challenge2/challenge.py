import numpy as np
"""
DESCRIPTION : stateAtNextTime allows to provide the system state (= vector [PE(m+1), PI(m+1), PO(m+1)]) 
at time m+1 knowing the state of the system at the previous time ([PE(m), PI(m), PO(m)]) and the changing 
state matrix A. 
 
INPUTS : 
    - A: A 3x3 numpy array which describes the system 
    - Pm: A 3x1 numpy array which describes the state of the system at time m
OUTPUTS :
    - A 3x1 numpy array which describes the state of the system at time m+1
"""
def stateAtNextTime(A, Pm):
    A = np.array(A)
    B = np.array(Pm)
    def multiply(A,B):
        "MULTIPLICATION MATRICIELLE"
        # Cette fonction matrice génère la matrice de sortie après la multiplication
        def matrice(A,B):
            matrix=[]
            for i in range(len(A)):
                l=[]
                for j in range(len(B[0])):
                    l.append(0)
                matrix.append(l)
            return matrix
        m=matrice(A,B)
        #Verifie si les deux matrices ont la même dimension sinon lève une exception au else 
        if len(A[0])== len(B):
            #Parcours les lignes de la première matrice
            for i in range(len(A)):
                #Parcours les lignes de la deuxième matrice
                for j in range(len(B)):
                    #Parcours les colonnes de la deuxième matrice
                    for k in range(len(B[0])):
                        m[i][k]+= A[i][j] * B[j][k]
            return m
        else:
            raise Exception('Dimension mismatch')
    return multiply(A,B)
        
#print(stateAtNextTime( [[1/2, 1/4 ,1/6], [1/2 ,1/3 ,1/6], [0 ,3/4, 0 ]],[[2],[49],[6]]))


"""
DESCRIPTION : stateAtAnyTime allows to provide the system state (= vector [PE(m), PI(m), PO(m)]) 
at time m knowing the initial state of the system ([PE(0), PI(0), PO(0)]) and the changing state matrix A. 

INPUTS : 
    - A: A 3x3 numpy array which describes the system 
    - P0: A 3x1 numpy array which describes the initial state of the system (m=0)
    - m: the time at which we want to describe the system
OUTPUTS :
    - A 3x1 numpy array which describes the state of the system at time m>0
"""

def stateAtAnyTime(A, P0, m):
    if m==0:
        raise ValueError("m doit être strictement superieur à 0")
    if m==1:
        return stateAtNextTime(A,P0)
    resultat = stateAtNextTime(A,A)
    for i in range(1,m-1):
        resultat = stateAtNextTime(resultat,A)
    return stateAtNextTime(resultat,P0)


print(stateAtAnyTime( [[1/2, 1/4 ,1/6], [1/2 ,1/3 ,1/6], [0 ,3/4, 0 ]],[[2],[49],[6]],100))




import matplotlib.pyplot as plt

def graphe(A,Pm,m):
    matrix,x,p1,p2,p3=[],[],[],[],[]
    for i in range(1,m+1):
        matrix.append(stateAtAnyTime(A,Pm,i))
    for i in range(m):
        p1.append(matrix[i][0][0])
        p2.append(matrix[i][1][0])
        p3.append(matrix[i][2][0])
        x.append(i+1)
    plt.figure(figsize=(10, 6))
    plt.plot(x,p1 , 'r',label="PE")
    plt.plot(x,p2 , 'b',label="PI")
    plt.plot(x,p3, 'y',label="PO")
    plt.legend()    
    plt.ylabel('Evolution au cours du temps(m)')
    plt.xlabel('Nombres de semaines(m)')
    plt.show()


#print(graphe([[1/2, 1/4 ,1/6], [1/2 ,1/3 ,1/6], [0 ,3/4, 0 ]],[[2],[49],[6]],10))




#Fonction Auxilliaire
def mat_normale(P):
    m,l=[],[]
    j=0
    for i in range(len(P)):
        m.append(P[i])
        j+=1
        if j==3:
            l.append(m)
            m=[]
            j=0
    return l

def inverse():
    l1 = np.array([[0.576874357444842, -0.332169699847419, 0.237285155552940],
                   [0.634088276319889, 4.66256114936158e-64, 0.123357066247932],
                   [0.514925269875419, 0.996509099542256, -1.02535280374507]])
    p_inv = np.linalg.inv(l1)
    return p_inv
#print(inverse())

from sympy import Matrix 

"""
DESCRIPTION : stateAtAnyTime_withDiagonalization allows to provide the system state (= vector [PE(m), PI(m), PO(m)]) 
at time m knowing the initial state of the system ([PE(0), PI(0), PO(0)]) and the diagonalization of the 
the changing state matrix A.

INPUTS : 
    - P, D, P_inv: matrices obtained by the diagonalization of A such that A = P*D*P_inv
    - P0: A 3x1 numpy array which describes the initial state of the system (m=0)
    - m: the time at which we want to describe the system
OUTPUTS :
    - A 3x1 numpy array which describes the state of the system at time m>0
"""
def mat(A):
    A=Matrix(A)
    P,D = A.diagonalize()
    D1=mat_normale(D)
    P1=mat_normale(P)
    return P1
    

#print(mat([[1/2, 1/4 ,1/6], [1/2 ,1/3 ,1/6], [0 ,3/4, 0 ]]))

   


def stateAtAnyTime_withDiagonalization(P, D, P_inv, P0, m):
    mul = stateAtNextTime(stateAtNextTime(P,D),P_inv)
    mul1 = mul
    for i in range(1,m):
        mul1 = stateAtNextTime(mul,mul1)
    return stateAtNextTime(mul1,P0)



print(stateAtAnyTime_withDiagonalization([[0.576874357444842, -0.332169699847419, 0.237285155552940],
                                          [0.634088276319889, 4.66256114936158e-64, 0.123357066247932],
                                          [0.514925269875419, 0.996509099542256, -1.02535280374507]],
                                            [[0.923563544191518, 0, 0], [0, 1.57653599766961e-64, 0],[0, 0, -0.0902302108581850]],
                                             [[ 0.77780489 , 0.65889959,  0.2592683 ],
                                              [-4.51576408 , 4.51576408, -0.50175156],
                                              [-3.99812493 , 4.71962824, -1.33270831]],[[2],[49],[6]],100))


import time


# Timing for Method 1 - Without Diagonalization
start = time.process_time()
pos1 = stateAtAnyTime([[1/2, 1/4 ,1/6], [1/2 ,1/3 ,1/6], [0 ,3/4, 0 ]],[[2],[49],[6]],2000)
stop = time.process_time()
print((stop-start)*1000)

# Timing for Method 2 - With Diagonalization
start = time.process_time()
pos2 = stateAtAnyTime_withDiagonalization([[0.576874357444842, -0.332169699847419, 0.237285155552940],
                                          [0.634088276319889, 4.66256114936158e-64, 0.123357066247932],
                                          [0.514925269875419, 0.996509099542256, -1.02535280374507]],
                                            [[0.923563544191518, 0, 0], [0, 1.57653599766961e-64, 0],[0, 0, -0.0902302108581850]],
                                             [[ 0.77780489 , 0.65889959,  0.2592683 ],
                                              [-4.51576408 , 4.51576408, -0.50175156],
                                              [-3.99812493 , 4.71962824, -1.33270831]],[[2],[49],[6]],2000)


stop = time.process_time()
print((stop-start)*1000)
print()

A = stateAtNextTime([[1,1,-1], [1,0,1], [1,-1,0]], [[1,0,0], [0,-2,0], [0,0,-2]])
B = stateAtNextTime(A,[[ 0.33333333,0.33333333,0.33333333],[ 0.33333333 , 0.33333333 ,-0.66666667],
                                                      [-0.33333333 , 0.66666667, -0.33333333]])

print(B)
