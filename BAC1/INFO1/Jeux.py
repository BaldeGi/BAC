#Le jeu du plus ou moins
#Le jeu du plus ou moins
import os
from tkinter import*
from random import randrange
l=[]
print("\t\t\t\t=== LE JEU DU PLUS OU MOINS ===\n\n")
def facile():
    compteur=0
    nbreproposer=0
    nbremyst=randrange(26)
    while nbreproposer!=nbremyst:
        print("Entrez le nombre : ")
        
        nbreproposer=input()
        nbreproposer=int(nbreproposer)
        l.append(nbreproposer)
        compteur+=1
        if compteur!=4:
            if nbreproposer<0 or nbreproposer>25:
                print("ERREUR :Votre nombre ne'est pas dans l'intervalle demandée")
            
            elif nbreproposer > nbremyst:
                print("Le nombre est trop grand")
                
            elif nbreproposer<nbremyst:
                print("Le nombre est trop petit")
            
            else:
                print("Félicitations, vous avez gagné au bout de {} essaies et voici les nombres que vous avez proposez {} "  .format(compteur, l))
        else :
            print("Le Nombre d'essais qui est de 3 est atteints")
            break
    #On met les système en pause
    os.system("Pause")
def normale():
    compteur=0
    nbreproposer=0
    nbremyst=randrange(51)
    while nbreproposer!=nbremyst:
        print("Entrez le nombre : ")
        
        nbreproposer=input()
        nbreproposer=int(nbreproposer)
        l.append(nbreproposer)
        compteur+=1
        if compteur!=6:
            if nbreproposer<0 or nbreproposer>50:
                print("ERREUR: Votre nombre ne'est pas dans l'intervalle demandée")
            
            elif nbreproposer > nbremyst:
                print("Le nombre est trop grand")
                
            elif nbreproposer<nbremyst:
                print("Le nombre est trop petit")
            
            else:
                print("Félicitations, vous avez gagné au bout de {} essaies et voici les nombres que vous avez proposez {} "  .format(compteur, l))
        else:
             print("Le Nombre d'essais qui était de 5 est atteints")
             break
    #On met les système en pause
def difficile():
    compteur=0
    nbreproposer=0
    nbremyst=randrange(101)
    while nbreproposer!=nbremyst:
        print("Entrez le nombre : ")
        
        nbreproposer=input()
        nbreproposer=int(nbreproposer)
        compteur+=1
        l.append(nbreproposer)
        if compteur!=9:
            if nbreproposer<0 or nbreproposer>100:
                print("ERREUR :Votre nombre ne'est pas dans l'intervalle demandée")
            
            elif nbreproposer > nbremyst:
                print("Le nombre est trop grand")
                
            elif nbreproposer<nbremyst:
                print("Le nombre est trop petit")
            
            else:
                print("Félicitations, vous avez gagné au bout de {} essaies et voici les nombres que vous avez proposez {} "  .format(compteur, l))
        else:
             print("Le Nombre d'essais  qui est de 8 est atteints")
             break
    #On met les système en pause
    os.system("Pause")
 
fen = Tk()
fen.title('PLUS OU MOINS')
     
bou1 = Button(fen, text= 'Facile', command = facile).pack(side=BOTTOM)
bou1 = Button(fen, text= 'Moyen', command = normale).pack(side=BOTTOM)
bou1 = Button(fen, text= 'Difficile', command = difficile).pack(side=BOTTOM)


fen.mainloop()
            
            
              


