def readfile(filename):
    """
    pre: filename est un nom de fichier
    post: retourne une liste des lignes du fichier filname ,tous les carateres inclus
    """
    try:
        l=[]
        with open(filename,"r") as file:
            for line in file:
                l.append(line.strip())
            return l
    except FileNotFoundError:
        return -1
    except:
        return []
    
print(readfile('filename.txt'))
    

def get_words(line):
    """
    pre: line est une chaines de caractere
    post: retourne une liste des mots dans la chaîne, en minuscules, et sans ponctuation.
    """
    ponct=[",",".","!","?",":",";","\t","'"]
    new_lines=""
    lines=line.lower()
    for i in lines:
        if i not in ponct:
            new_lines+=i
        elif i=="\t":
            new_lines+=" "
    new_lines=new_lines.split()
    return new_lines



def create_index(filename):
    """
    pre: filename est un nom de fichier
    post: retourne des dictionnaires imbriqués.La cle du premier dictionnaire etant un
    mot se trouvant dans filename, la valeur est un second dictionnaire dont la cle
    est un index du mot et la valeur est le nombre de fois que ce mot se trouve à cet index

    Exemple: {"while": {0: 1}}
    """
    lst=[]
    dic={}
    lste=readfile(filename)
    for i in range(len(lste)):
        lst.append(get_words(lste[i]))

    for u in lst:
        for v in u:
            dic[v]={}
        
            for i in range(len(lst)):
                a=0
                for j in range(len(lst[i])):
                    
                    if v==lst[i][j]:
                        
                        a+=1
                if a>0:
                    dic[v][i]=a
    return dic

print(create_index('filename.txt'))
 

def get_lines(words,index):
    """
    pre: words est une liste de mots , index est un dictionnaire imbriqué({"while": {0: 1}}
    post: retourne les identifiants des lignes qui contiennent tous les mots spécifiés dans la liste words
    
    Exemple: ["the","republic"] doit retourner la liste [0] puisque les deux mots se trouvent à la première ligne.
    """
    l=[]
    liste=[]
    index=create_index('filename.txt')
    line=index.get(words[0],[])
    temp=dict(line)
    for mot in words[1:]:
        if mot in index:
            for i in line:
                if i not in index[mot]:
                    del temp[i]
            line=dict(temp)
        else:
            line=None
            break
    if line!=None:
        for i in line:
            liste.append(i)
        return liste
    return []

print(get_lines(['while','the','congress'],create_index('filename.txt')))   
                 


def execute():
    """
    pre: -
    post: Cette fonction retourne les identifiants des lignes qui contiennent tous les mots spécifiés en ligne de commande
    si ils se trouventt dans le dictionnaire.
    """
    
    exit=False
    while not exit:
        filename=input("Entrez le nom d'un fichier: ")
        command=input("Entrez des mot separés par un espace :  ").split(" ")
        if command[0]=="help":
            print("Il existe une commande get_lines qui vous affiche la ligne où se situe tous les mots de la liste que vous mettez en commande. Cette liste est une liste de mot séparés espaces")
        if command[0]=="exit":
            exit=True
        else:
            for i in command:
                if i not in create_index(filename):
                    print("Vous avez une liste vide car un ou plusieurs des mots que vous avez rentrez en commande n'existent pas dans le dictionnaire")
                    break
            try:
                print(get_lines(command,filename))
            except:
                print("Fichier inexistant")
                
            
        
            
execute()

