matrix = [
    [8, 11, 4],
    [7, 12, 9],
    [0, -6, 0],
]

sum_even = 0
i=0
while i<len(matrix):
    j=0
    while j<len(matrix[i]):
        if matrix[i][j]%2==0:
            sum_even+=matrix[i][j]
        j+=1
    i+=1
print(sum_even)