def sum(list):
    somme=0
    for i in range(len(list)):
        if type(list[i])==int or type(list[i])==float:
            somme+=list[i]
    return somme
    
print(sum(['a',3,2,3,4,1.3,'e']))