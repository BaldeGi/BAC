def diff_count(lst):
    l=[]
    count=0
    if lst!=[]:
        for i in lst:
            if i not in l:
                l.append(i)
                count+=1
        return count
    else:
        return 0
            
print(diff_count([3,3,3,2,3,3,4]))