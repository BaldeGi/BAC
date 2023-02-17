#FONCTION QUI MARCHE SUR THONNY MAIS PAS SUR INGINIOUS

def lecture():
    """
    post: Ouvre le fichier si il existe oubien retourn -1
    """
    l=[]
    try:
        with open("filenames.txt","r") as file:
            liste=file.readlines()
            for i in range(len(liste)):
                l.append(liste[i].strip("\n").split(" "))
            return l
    except OSError:
        return -1
def valid_lines():
    """
    post: Verifie que les lignes ne contiennent chacune qu'un element
    """
    l,listes=[],[]
    l=lecture()
    for line in range(len(l)):
        if len(l[line])==1:
            listes.append(l[line])
    if listes!=[]:
        return listes
    else:
        return -1
def valid_element():
    """ post: Verifie que chaque ligne n'est pas un str et que c'est un float
    """
    try:
        listes=valid_lines()
        lst,lste=[],[]
        for line in range(len(listes)):
            for j in range(len(listes[line])):
                lst.append(listes[line][j].split('.'))
        for i in range(len(lst)):
            if len(lst[i])==2:
                index=i
                lste.append(listes[index])
        if lste!=[]:
            return lste
        else:
            return -1
    except:
        return -1
def get_max(filename):
    """
    return le plus grand float >0
    """
    try:
        max_value=[]
        lste=valid_element()
        for i in range(len(lste)):
            for j in range(len(lste[i])):
                max_value.append(float(lste[i][j]))
        for i in range(len(max_value)):
            if max(max_value)<0:
                return -1
        return max(max_value)
    except:
        return -1
print(get_max("filenames.txt"))


#FONCTION QUI MARCHE SUR INGINIOUS ET THONNY

def get_max(filenames):
    l,max_value=[],[]
    listes,liste=[],[]
    lst,lste=[],[]
    try:
        with open(filenames,"r") as file:
            liste=file.readlines()
            for i in range(len(liste)):
                l.append(liste[i].strip("\n").split(" "))
    except OSError:
        return -1
    try:
        for line in range(len(l)):
            if len(l[line])==1:
                listes.append(l[line])

        for line in range(len(listes)):
            for j in range(len(listes[line])):
                lst.append(listes[line][j].split('.'))
        for i in range(len(lst)):
            if len(lst[i])==2:
                index=i
                lste.append(listes[index])
        if lste!=[]:
            for i in range(len(lste)):
                for j in range(len(lste[i])):
                    max_value.append(float(lste[i][j]))
            for i in range(len(max_value)):
                if max(max_value)<0:
                    return -1
                return max(max_value)
        else:
            return -1
                    
    except ValueError:
        return -1
print(get_max("filenames.txt"))

#FONCTION QUI MARCHE SUR INGINIOUS ET THONNY

def get_max(filename):
    try:
        with open(filename,"r") as f:
            l=[]
            for i in f:
                try:
                    if float(i)>=0 :
                        l.append(float(i))
                except ValueError:
                    pass
            if l==[]:
                return -1
            return max(l)
    except OSError:
        return -1
print(get_max("filenames.txt"))

