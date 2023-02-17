from Q_Anonymous import*
from Q_Anonimous2 import*
def  collect(file):
    d,lst={},[]
    with open(file , "r") as f:
        l = f.read().split()
    for i in l:
        lst.append(treatment(extract(i)).strip())
    for i in range(len(lst)):
        lst[i]=lst[i].split()
    for i in lst:
        for j in i:
           d[j]=d.get(j,0)+1
    return d
    

print(collect("anonymous.txt"))





