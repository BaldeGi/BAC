def sorted_l(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)):
            if a_list[i]>a_list[j] and i<j:
                a_list[i],a_list[j]=a_list[j],a_list[i]
            else:
                a_list[i]=a_list[i]
    sorted_list=a_list
    return (sorted_list)

print(sorted_l([2,3,0,1]))
l=[2,3,0,1]
l=sorted(l)
print(l)
