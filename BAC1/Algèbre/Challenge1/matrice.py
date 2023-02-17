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
        
   
print(multiply([[2.0,4.0,62.0]],[[42.0],[8.0],[9.0]]))
print(multiply([[4,5],[6,7]],[[8,9],[10,11]]))
print(multiply( [[1/2, 1/4 ,1/6], [1/2 ,1/3 ,1/6], [0 ,3/4, 0 ]],[[2],[49],[6]]))

 
A = multiply([[2,-2],[2,2]],[[1,0],[0,3]])
print(multiply(A,[[1/4,1/4],[-1/4,1/4]]))




    

    













