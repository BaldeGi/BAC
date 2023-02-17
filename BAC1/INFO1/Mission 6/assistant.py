def file(commande):
    with open(commande,"r") as file:
        return file

def info(filename):
    with open(filename,"r") as fichier:
        lines=0
        for line in fichier.readlines():
            lines+=1
    with open(filename,"r") as fichier:
        caract=len(fichier.read())
    assist=(str(lines) + " lignes " + str(caract) + " caractères")
    return assist


def dictionnary(filename):
    l=[]
    with open(filename,"r") as fichier:
        dictionnaire=fichier.readlines()
        for line in range(len(dictionnaire)):
            dico=dictionnaire[line].strip("\n").split(",")
            l.append(dico)
        l.sort()
        for i in range(len(l)):
            if type(int(l[i][1]))!=int:
                return False
        return l
            

def search(filename,word):
    for line in(dictionnary(filename)):
        for lines in line:
            if word==lines:
                return True    
    return False
            
def somme(valeurs):
    valeurs=valeurs.split(" ")
    somme=0
    for i in valeurs:
        if type(int(i))==int:
            somme+=int(i)
    return somme
    
def avg(valeurs):
    longueur=len(valeurs.split(" "))
    average=somme(valeurs)/longueur
    return average


def commandes():
    exit=False
    while not exit:
        command=((input("Entrez une commande sans espace à la fin ou entrer help pour voir les commandes disponibles: ")))
        if (command)=="file":
            try:
                commande=input("Entrez le nom du fichier: ")
                print(file(commande))
            except:
                print("Nom du fichier incorrect ou inexistant")
        if command=="info":
            fichier=((input("Entrez le nom du fichier: ")))
            try:
                print(info(fichier))
            except:
                print("Verifiez qu'il s'agit bien d'un fichier existant")
        if command=="dico":
            dico=((input("Entrez le nom du dictionnaire: ")))
            try:
                if dictionnary(dico):
                    print("Il s'agit bien d'un dictionnaire")
            except:
                print("Il ne s'agit pas d'un dictionnaire")
        if command=="search":
            filename=(input("Entrez le dictionnaire dans lequel vous le cherchez: "))
            try:
                word=(input("Entrez le mot que vous cherchez: "))
                if search(filename,word)==True:
                    print(word," , se trouve bien dans le dictionnaire")
                else:
                    print(word," , ne se trouve pas dans le dictionnaire")
            except:
                print("Le fichiers n'est pas un dictionnaire ou n'existe pas")
        if command=="sum":
            valeurs=(input("Entrez la suite de nombre: "))
            try:
                print(somme(valeurs))
            except:
                print("Verifiez que ce sont bien des entiers que vous avez entré comme valeurs")
            
        if command=="avg":
            valeurs=((input("Entrez la suite de nombre: ")))
            try:
                print(avg(valeurs))
            except:
                print("Verifiez que ce sont bien des entiers que vous avez entré comme valeurs")
        if command=="help":
            print("Les commandes sont : file,info,dico,search,sum,avg,exit.Entrer une commande et suivez les instructions")

        if command=="exit":
            exit=True
            
        if command!="file" and command!="sum" and command!="avg" and command!="dico" and command!="search" and command!="info" and command!="exit" and command!="help":
            print("Command_error: Verifiez qu'il n'y a d'espace ni avant ni après la commande")

commandes()

if __name__ == "__main__":
    commandes()


 

