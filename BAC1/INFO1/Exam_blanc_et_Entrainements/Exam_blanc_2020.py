def mix(l):    # Ne pas effacer cette ligne
    """
    @pre:    l est une liste d'entiers
            la taille n de cette liste est un nombre pair
    @post:   retourne une liste r d’entiers
            la liste retournée r a la même taille n
            pour chaque index 0 ≤ i < n où i est pair on a la
            correspondance suivante entre les deux listes :
                r[i] = l[i//2]
                r[i+1] = l[n-1-(i//2)]
    """
    r=[]
    i,j=0,-1
    while i<len(l):
        r.append(l[i])
        r.append(l[j])
        if len(r)==len(l):
            break
        else:
            i+=1
            j+=-1
    return r

def combien(n):    # Ne pas effacer cette ligne
    """
    @pre:  n est un nombre entier > 0
    @post: retourne le nombre de series d’entiers consecutifs
           strictement positifs dont la somme est egale a n
    """
    indice=[]
    l=[]
    count=0
    for i in range(1,n+1):
        somme=0
        for j in range(i,n+1):
            somme+=j
            if somme==n:
                count+=1
    return count

def somme_des(n):    # Ne pas effacer cette ligne
    """
    @pre:  n est un nombre entier > 0
    @post: retourne un dictionnaire avec comme différentes clés
           chaque somme possible des valeurs des dés,
           et comme valeur associée à cette clé e,
           la liste des tuples des valeurs des dés qui addtionnées donnent e
    """
    l=[]
    d={}
    for i in range(2,(n*2)+1):
        l.append(i)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i+j in l:
                d[i+j]=d.get((i+j),[])+[(i,j)]
    return d

def acrostiche(file_name): # Ne pas effacer cette ligne
    """
    @pre:  file_name est le nom d'un fichier de texte
    @post: Retourne une chaîne de caractères contenant la première lettre
          de chaque ligne dans le fichier de texte,
          pour les lignes qui contiennent au moins un caractère.
          Retourne -1 en cas d'erreur d'accès au fichier.
    """
    mot=""
    try:
        with open(file_name) as file:
            l=file.read().split("\n")
        for i in range(len(l)):          #On peut aussi utiliser des boucles imbriquées while 
            for j in range(len(l[i])):
                if l[i]!="":
                    if l[i][j].isalpha():
                        mot+=l[i][j]
                        break
        return mot
    except:
        return -1
    
    
class SudokuPuzzle:
    def __init__(self,dimension) :
        """
        Crée un SudokuPuzzle de dimension `dimension` avec tous les éléments initialisés à 0.
        """
        self.dimension = dimension
        self.carres = [ [ SudokuCarre(x,y,dimension) \
                          for x in range (dimension) ] \
                          for y in range (dimension)]
        
        

    def get_carre(self,x,y) :
        """
        Retourne le SudokuCarre qui se trouve à la position (x, y) dans ce Sudoku.
        """
        return self.carres[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le Sudoku.
        """
        s = ""
        for y in range(len(self.carres)) :
            for x in range (len(self.carres[y])) :
                s += str(self.get_carre(x,y))
            s += "\n"
        return s
    
    def get_carre_valeurs(self, x, y):    # Ne pas effacer cette ligne
        """
        @pre:  0 ≤ x < N
               0 ≤ y < N
        @post: retourne une liste de toutes les valeurs apparaissant dans le SudokuCarre
               qui se trouve à la position (x, y) du puzzle Sudoku
               Si une valeur apparaît plusieurs fois dans ce carré,
               elle se retrouvera plusieurs fois dans la liste retournée.
        """
        lst=[]
        l=self.get_carre(x,y).cells
        for i in range(len(l)):
            for j in range(len(l[i])):
                lst.append(l[i][j])
        return lst
    
    def get_ligne(self, ligne):    # Ne pas effacer cette ligne
        """
        @pre:  0 ≤ ligne < N * N
        @post: retourne une liste de toutes les valeurs apparaissant
               à une certaine ligne du puzzle Sudoku
               Si une valeur apparaît plusieurs fois sur une ligne
               elle se retrouvera plusieurs fois dans la liste retournée
        """
        values = []
        h_carre = ligne//self.dimension
        ligne_carre = ligne%self.dimension
        for l_carre in range(self.dimension):
            carre = self.get_carre(l_carre, h_carre)
            for long in range(self.dimension):
                values.append(carre.get_val(long, ligne_carre))
        return values
    
    
    def get_colonne(self, colonne):    # Ne pas effacer cette ligne
        """
        @pre:  0 ≤ colonne < N * N
        @post: retourne une liste de toutes les valeurs apparaissant
               à une certaine colonne du puzzle Sudoku
               Si une valeur apparaît plusieurs fois sur une colonne
               elle se retrouvera plusieurs fois dans la liste retournée
        """
        values = []
        l_carre = colonne//self.dimension
        colonne_carre = colonne%self.dimension
        for h_carre in range(self.dimension):
            carre = self.get_carre(l_carre, h_carre)
            for haut in range(self.dimension):
                values.append(carre.get_val(colonne_carre, haut))
        return values
        
    def verify_list(self, l):
        """
        @pre: une liste l triée
        @post: retourne un booléen
               True si la liste est composé de chaque élément entre 1 et le carré de la dimension du Sudoku
               False sinon
        """
        size = self.dimension*self.dimension
        for elem in range(1, size+1):
            if elem != l[elem-1]:
                return False
        return True

 
    def est_correct(self):    # Ne pas effacer cette ligne
        """
        @pre:  ce Sudoku est bien formé, de dimension self.dimension
        @post: retourne un booléen
               True si le puzzle est correct
               False sinon
        """
        size = self.dimension*self.dimension
        # Vérification des lignes
        for line in range(size):
            if not self.verify_list(sorted(self.get_ligne(line))):
                return False
        
        # Verification des colonnes
        for col in range(size):
            if not self.verify_list(sorted(self.get_colonne(line))):
                return False
            
        # Vérification des carrés
        for hauteur in range(self.dimension):
            for longueur in range(self.dimension):
                if not self.verify_list(sorted(self.get_carre_valeurs(longueur, hauteur))):
                    return False
                
        return True
        

class SudokuCarre:

    def __init__(self,x,y,dimension) :
        """
        Crée un SudokuCarre de taille `dimension` x `dimension`, avec toutes ses valeurs initialisées à 0.
        """
        self.xcoord_carre = x
        self.ycoord_carre = y
        self.cells = [ [ 0 for x in range(dimension) ]
                        for y in range(dimension) ]

    def set_val(self,x,y,val) :
        """
        Assigne une valeur `val` à la cellule se trouvant à la position (x, y) de ce carré.
        """
        self.cells[y][x] = val

    def get_val(self,x,y) :
        """
        Retourne la valeur qui se trouve à la position (x, y) de ce carré.
        """
        return self.cells[y][x]

    def __str__(self):
        """
        Retourne un texte permettant de représenter le contenu de ce carré.
        """
        s = "carré (" + str(self.xcoord_carre) + "," + str(self.ycoord_carre) + ") : "
        s += str(self.cells)
        s += " "
        return s
    

if __name__ == '__main__':
    print("----Mix----")
    print(mix([1,2,3,4]))
    print(mix([1,2,3,4,5,6,7,8]))
    print()
    print("----Combien----")
    print(combien(100))
    print()
    print("----Somme_n----")
    print(somme_des(4))
    print()
    print("----Acrostiche----")
    print(acrostiche("message.txt"))
    print(acrostiche("message2.txt"))
    print()
    print("----Classe-Sudoku----")
    # créer un puzzle Sudoku vide de dimension 2
    p = SudokuPuzzle(2)
    # remplir les carrés et leurs valeurs
    # initiliaser le carré à la position (0,0)
    p.get_carre(0,0).set_val(0,0,1)
    p.get_carre(0,0).set_val(1,0,4)
    p.get_carre(0,0).set_val(0,1,3)
    p.get_carre(0,0).set_val(1,1,2)
    # initiliaser le carré à la position (1,0)
    p.get_carre(1,0).set_val(0,0,3)
    p.get_carre(1,0).set_val(1,0,2)
    p.get_carre(1,0).set_val(0,1,4)
    p.get_carre(1,0).set_val(1,1,1)
    # initiliaser le carré à la position (0,1)
    p.get_carre(0,1).set_val(0,0,4)
    p.get_carre(0,1).set_val(1,0,1)
    p.get_carre(0,1).set_val(0,1,2)
    p.get_carre(0,1).set_val(1,1,3)
    # initiliaser le carré à la position (1,1)
    p.get_carre(1,1).set_val(0,0,2)
    p.get_carre(1,1).set_val(1,0,3)
    p.get_carre(1,1).set_val(0,1,1)
    p.get_carre(1,1).set_val(1,1,4)
    # imprimer le sudoku
    print(p)
    # 1 4 | 3 2
    # 3 2 | 4 1
    # ---------
    # 4 1 | 2 3
    # 2 3 | 1 4

    
    print(p. get_carre_valeurs(0, 1))
    # par exemple: [4, 1, 2, 3]
    print()
    
    print(p.get_ligne(3))
    # par exemple: [2, 3, 1, 4]
    print()
    
    print(p.get_colonne(2))
    # par exemple: [3, 4, 2, 1]
    print()
    
    print(p.est_correct())
    
   
    
    
    

        