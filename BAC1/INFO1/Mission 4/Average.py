def average(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
        avg=sum/len(list)
    return avg
print(average([66, 93, 16, 41, 55, 58, 39, 55, 68, 76, 74, 94, 89]))