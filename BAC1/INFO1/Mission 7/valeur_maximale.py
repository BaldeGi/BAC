def create_dict_max(l):
    d={}
    for i,j in l:
        if j>d.get(i,j-1):
            d[i]=j
    return d
print(create_dict_max([(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]))

#OU

def create_dict_max(l):
    d={}
    for i,j in l:
        if j>d.get(i,0):
            d[i]=j
    return d
        
    
print(create_dict_max([(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]))


