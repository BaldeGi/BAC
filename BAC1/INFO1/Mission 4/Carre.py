def carre(n):
    matrix=[]
    count=0
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(count)
            count+=1
    print(matrix)
carre(4)