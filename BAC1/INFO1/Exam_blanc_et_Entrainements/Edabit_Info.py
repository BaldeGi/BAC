#BUBBLE
def bubble_sort(l):
    nb_comparaison , nb_echg = 0 ,0
    for i in range(len(l)-1,0,-1):
        for j in range(1,i+1):
            nb_comparaison+=1
            if l[j-1]>l[j]:
                nb_echg+=1
                l[j],l[j-1]=l[j-1],l[j]
    return l , nb_comparaison,nb_echg


print(bubble_sort([65, 97, 43, 12, 29, 14, 99]))
print()

#SELECTION
def selection_sort(l):
    nb_comp , nb_echng = 0 , 0
    for i in range(len(l)):
        min = i
        #Recherche min dans le tableau restant
        for j in range(i+1,len(l)):
            nb_comp +=1
            if l[j]< l[min]:
                min = j
        if min != i:
            nb_echng+=1
            l[i] , l[min] = l[min] , l[i]
    return l,nb_comp,nb_echng

print(selection_sort([65, 97, 43, 12, 29, 14, 99]))
print()

#INSERTION ( Revoir)
def insertion_sort(l):
    nb_comp , nb_echng = 0 , 0
    for i in range(1,len(l)):
        key = l[i]
        j = i-1
        while j>=0 and l[j]>key:
            nb_comp+=1
            if j== i-1:
                nb_echng+=1
            l[j+1] = l[j]
            j-=1
            nb_echng+=1
        l[j+1] = key
    return l
    
    
print(insertion_sort([65, 97, 43, 12, 29, 14, 99]))

def mode(lst):
    mode = lst[0]
    count0 = 0
    for i in lst:
        count = 0
        for j in lst:
            if j==i:
                count+=1
        if count0<count:
            count0 = count
            mode = i
    return mode
        
 
print(mode(insertion_sort( [6, 0, 4, 8, 7, 6, 4, 7, 5, 9, 3, 8, 2, 4, 2, 1])))

    
 
def readfile(filename):
    with open(filename) as file:
        return file.readlines()
       
print(readfile("test.txt"))


def get_words(line):
    line = line.lower()
    line = line.split()
    l , mot = [],""
    ponct = [",",".","?","!"]
    for i in line:
        for j in i:
            if not j in ponct:
                mot+=j
        l.append(mot)
        mot =""
    return l
    
print(get_words("Turmoil. has engulfed the Galactic Republic."))


def create_index(filename):
    d = {}
    sent = readfile(filename)
    lst = []
    for i in sent:
        lst.append(get_words(i))
    for i in range(len(lst)):
        m = {} 
        for j in range(len(lst[i])):
            d[lst[i][j]] = m
            for k in range(len(lst)):
                if lst[k].count(lst[i][j]) >=1:
                    m[k] = lst[k].count(lst[i][j])
            m={} 
    return d
    
print(create_index("test.txt"))


def concat_similar_values(l):
    mot=""
    liste = []
    if len(l)==1: return l
    if l==[]: return []
    for i in range(len(l)-1):
        nb = l[i]
        if nb != l[i+1]:
            mot +=str(l[i])
            liste.append(int(mot))
            mot = ""
        else : mot +=str(l[i])
    mot+=str(l[i+1])
    liste.append(int(mot))
    return liste

def concat_similar_values(l):
    mot=""
    liste = []
    if len(l)==1: return l
    if l==[]: return []
    while l!=[]:
        if len(l) == 1:
            mot+=str(l[0])
            liste.append(int(mot))
            del l[0]
        elif l[0]==l[1]:
            mot=mot+str(l[0])
            del l[0]
        else:
            mot=mot+str(l[0])
            del l[0]
            liste.append(int(mot))
            mot= " "
    return liste
            
        

          
print(concat_similar_values([]) == [])                                            # imprime True
print(concat_similar_values([5]) == [5])                                          # imprime True
print(concat_similar_values([1,1,35,2,2,3,3,3,7,7,7,7,4,3,4,4]) == [11, 35, 22, 333, 7777, 4,3,44]) # imprime True
print(concat_similar_values([10,10,20,123,123]) == [1010, 20, 123123])                   # imprime True
    
    
    
    
    
    
    
    
    
    
    