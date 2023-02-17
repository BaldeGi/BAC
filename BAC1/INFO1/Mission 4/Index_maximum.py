def maximum_index(lst):
    l=[]
    if lst!=[]:
        maximum=lst[0]
        for i in range(len(lst)):
            if maximum < lst[i]:
                maximum=lst[i]
                index=i
        return index
    else:
        return None
print(maximum_index([64, 533, 40]))



