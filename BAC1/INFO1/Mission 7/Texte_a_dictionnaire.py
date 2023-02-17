def create_dictionary(filename):
    d={}
    with open(filename,"r") as file:
        liste=file.read().strip("\n").split()
        for i in range(len(liste)):
            d[liste[i]]=liste.count(liste[i])
        return d
    
       
print(create_dictionary("text.txt"))
    
def occ(dictionary, word):
    for i in dictionary:
        if i==word:
            return dictionary[i]
    return 0
#Ou comme ça
    
def occ(dictionary, word):
    return dictionary.get(word,0)

print(occ(create_dictionary("text.txt"),"mot"))
    
    
    
   
