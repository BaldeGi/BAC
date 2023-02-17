def triangle(n):
    matrix=[]
    for i in range(n):
        l=[]
        for j in range(i+1):
            l.append(j)
        matrix.append(l)
    print(matrix)
triangle(5)
        