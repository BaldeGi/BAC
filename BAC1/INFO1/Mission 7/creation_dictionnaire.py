def create_dict(l):
    d={}
    for i in l:
        d[i[0]]=d.get(i[0],[])+[i[1]]
    return d
    
    
    
print(create_dict( [(2.0, 5.0), (8.0, 12.0), (10.0, 40.0), (8.0, 50.0), (8.0, 50.0)]))