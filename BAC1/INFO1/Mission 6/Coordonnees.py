def write_coordinates(filename, l):
    """
    pour créer un fichier qui contient les coordonnées de la liste l dans le format suivant:
    0.5,0.5
    0.1,0.3
    0.4,0.5
    """
    with open("filename_cord.txt","w") as file:
        l1 = ""
        for i in l:
            l1 += "{},{}\n".format(i[0],i[1])
        file.write(l1[:-1]) 
print(write_coordinates("filename_cord.txt", [(0.5,0.5),(0.1,0.3),(0.4,0.5)]))

#0U
def write_coordinates(filename, l):
    file = open(filename,"w")
    index = len(l)
    for x, y in l:
        if index != 1:
            file.write ( str(x) + "," + str(y) + "\n" )
        else:
            file.write(str(x)+","+str(y))
        index-=1
    file.close()
print(write_coordinates("filename_cord.txt", [(0.5,0.5),(0.1,0.3),(0.4,0.5)]))


def read_coordinates(filename):
    """
    lit les coordonnées du fichier filename, dans le format ci-dessus,
    et retourne une liste de tuples, comme donnée:[(0.5,0.5),(0.1,0.3),(0.4,0.5)]
    """
    with open("filename_cord.txt","r") as file:
        l=[]
        for line in file:
            t=line.split(",")
            l.append((float(t[0]),float(t[1])))
        return l
            
print(read_coordinates("filename_cord.txt"))











