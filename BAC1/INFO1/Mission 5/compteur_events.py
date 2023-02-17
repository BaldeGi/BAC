def count(events,i,j):
    count=0
    for event in events:
        if event==(i,j):
            count+=1
    return count
    
    
print(count([(0,1),(2,3),(0,1),(4,5),(1,2),(0,1),(1,1),(0,2),(1,1)],1,1))