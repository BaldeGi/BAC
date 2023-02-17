#sauvegarder les 4 entiers dans le fichier nommé filename
def save_data(filename, life, mana, position_x, position_y):
    with open(filename,"w") as file:
        file.write("{}\n{}\n{}\n{}".format(life, mana, position_x, position_y))
        


print(save_data("jeu.txt",2,4,6,8))

#retourne un tuple contenant les valeurs (life, mana, position_x et position_y précédemment sauvegardées
def load_data(filename):
    liste=[]
    with open("jeu.txt","r") as file:
        l=file.readlines()
        for i in range(len(l)):
            liste.append(l[i].strip("\n"))
        return int(liste[0]),int(liste[1]),int(liste[2]),int(liste[3])
        
 
print(load_data("jeu.txt"))

d = {0: {1: 1, 4: 1}, 1: [0, 1, 2]}

for v in d[0]:
  if d[1][2] == v:
    print ( "Found ")