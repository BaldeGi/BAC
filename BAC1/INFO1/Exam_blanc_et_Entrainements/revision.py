def diviseurs(l1,l2):
    """
    @pre: l1,l2 sont des listes d'entiers , potentiellement vides
    @post: retourne un dictionnaire avec comme differentes clés
           chaque element e de l1,et comme valuer associé a cette clés e,
           la liste des elements de l2 que l'on peut diviser par e.

    """
    d={}
    if l1==[]:
        return d
    elif l2==[]:
        for i in l1:
            d[i]=l2
        return d
    for i in l1:
        l=[]
        for j in l2:
            if j%i==0:
                l.append(j)
        d[i]=l
    return d

        
        
    

def rle(l):
    """
    @pre: l est uen liste d'elements , eventuellement vide,
          contenant soit de caractères , de chaines de caractères,
          ou de nombre entiers, mais ne contient pas d'elements None
    @post: retourne une nouvelle liste avec le codage run-length
           de la liste l comme décrit dans l'enoné ci-dessus

    """
    lst=[]
    count,counter=0,0
    for i in range(len(l)):
        first=l[counter]
        for j in range(counter,len(l)):
            if l[j]==first:
                count+=1
            else:
                lst.append((count,first))
                counter+=count
                count=0
                break
        if first==l[-1]:
            lst.append((count,first))
            break
    return lst
    
  

def est_correct(f):
    """
    @pre: f est le nom d'un fichier
    @post: retourne True si le fichier avec comme le nom f existe
           et si il a le format correct et False si il n'y a pas de
           fichier nommé f ou si ce fichier n'a pas le format correct
    """
    def aux(l):
        for i in l:
            if "," not in i or "@" not in i:
                return False
            else:
                if len(i.split(",")[0])!=8 or not i.split(",")[0].isdigit():
                    return False
        return True
    try:
        with open(f,"r") as file:
            l=file.read().split("\n")
            for i in l:
                if not aux([i]):
                    return False
            return True
    except:
        return False
    
    

    
    
    
def oxo(grille):
    """
    @pre: grille est une liste de m listes contenant chacune n valeurs,
          chaque valeur est soit le caractère "O", le caractère "X" , ou le
          le caractère " "
    @post: retourne le nombre total de combinaisons "O","X","O" dans des
           cas consecutives(soit horizontalement,verticalement, ou diagonalement)
           sur cette grille.
    """
    mot=""
    count=0
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            mot+=grille[i][j]
            if mot=="oxo":
                count+=1
                mot=""
        mot=""
        
    for i in range(len(grille[0])):
        for j in range(len(grille)):
            mot+=grille[j][i]
            if mot=="oxo":
                count+=1
                mot=""
        mot=""
    
    return count
            
from tkinter import *
 
# procédure générale de déplacement :
def avance(gd, hb):
    global x1, y1
    x1, y1 = x1 +gd, y1 +hb
    can1.coords(oval1, x1,y1, x1+30,y1+30)
 
# gestionnaires d'événements :
def depl_gauche():
    avance(-10, 0)
 
def depl_droite():
    avance(10, 0)
 
def depl_haut():
    avance(0, -10)

def depl_bas():
    avance(0, 10)
    
    

#------ Programme principal -------
 
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10        # coordonnées initiales
 
# Création du widget principal ("maître") :
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")
 
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=300,width=300)
oval1 = can1.create_oval(x1,y1,x1+30,y1+30,width=2,fill='red')
can1.pack(side=LEFT)
Button(fen1,text='Quitter',command=fen1.quit).pack(side=BOTTOM)
Button(fen1,text='Gauche',command=depl_gauche).pack()
Button(fen1,text='Droite',command=depl_droite).pack()
Button(fen1,text='Haut',command=depl_haut).pack()
Button(fen1,text='Bas',command=depl_bas).pack()
 
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()



if __name__=='__main__':
    print(diviseurs([3,5,10],[9,15,10,150]))
    print()
    print(rle(["A","A","A","C","C",1,1,1,"A","A","T","G","G"]))
    print()
    print(est_correct("filenames.txt"))
    print()
    print(est_correct("file.txt"))
    print()
    print(oxo([[ "o"," ","o" ],
               [ "x","x","x" ],
               [ "o"," ","o" ],
               [ "o","x","o" ]]))
    print()
    
    









 



