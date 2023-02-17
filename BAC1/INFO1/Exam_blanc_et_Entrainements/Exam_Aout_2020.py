def calembour( mot1, mot2 ) :
    """
    @pre: `mot1` et `mot2` sont des chaînes de caractères
    @post: retourne la concaténation de `mot1` et `mot2` en fusionnant
    la fin de `mot1` qui est identique au début de `mot2`. Par exemple,
    si mot1 = "lambada" et mot2 = "badaboum", "bada" est à la fin de `mot1`
    et au début de `mot2`, et donc le résultat est "lambadaboum".
    """
    i=-1
    while i>-len(mot1)-1:
        if mot1[i]==mot2[0]:
            pre=mot1[:i]
            same=mot1[i:]
            post=mot2[len(same):]
            if mot2[:len(same)]==same:
                return pre+same+post
            elif mot2[:len(same)]!=same and i>-len(mot1)-1:
                i-=1
            else:
                return mot1+mot2
        else:
            i-=1
    return mot1+mot2
        
            
def occurrences( p ):
    """
    @pre: `p` est une chaîne de caractères, potentiellement vide, contenant des mots
      (pour faciliter la question on peut supposer tous en minuscules) séparés par
      des espaces.
    @post: retourne un dictionnaire contenant, pour chaque mot apparaissant
      au moins une fois dans la chaîne `p`, un tuple avec comme première valeur
      le nombre de fois que ce mot apparaît dans la chaîne `p`, et comme deuxième
      valeur la position du premier occurrence de ce mot dans la phrase
      (on commence à compter les mots à partir de 1).
    """
    d={}
    l=[]
    p=p.split()
    for i in range(len(p)):
        if p[i] not in l:
            l.append(p[i])
            d[p[i]]=(p.count(p[i]),i+1)
    return d
        
    
class Date :
    """
    Une date, sous la forme (jour, mois, année).
    """

    def __init__(self,annee,mois,jour) :
        """
        @pre:  `annee` est un entier représentant une annee (ex: 2019)
               `mois` est un entier représentant un mois (ex: 1 pour janvier)
               `jour` est un entier entre 1 et 31 représentant le jour du mois
        @post: initialise cette Date avec les valeurs indiquées
               pour l'année, le mois et le jour.
        """
        self.__annee = annee
        self.__mois = mois
        self.__jour = jour

    def __str__(self) :
        """
        @post: Retourne un string représentant cet objet dans le format jour.mois.année
               (avec deux caractères pour le jour, deux pour le mois et quatre pour l'année)
        """
        return "{0:02}.{1:02}.{2:04}".format(self.__jour,self.__mois,self.__annee)

    def before(self, other):
        """
        @pre:  `other` est une Date
        @post: retourne True si cette Date est antérieure à `other`, False sinon.
        """
        assert isinstance(other, Date)
        if self.__annee < other.__annee:
            return True
        elif self.__annee > other.__annee:
            return False
        else :
            if self.__mois < other.__mois:
                return True
            elif self.__mois > other.__mois:
                return False
            else :
                if self.__jour < other.__jour:
                    return True
                elif self.__jour > other.__jour:
                    return False
                else :
                    # retourne False pour dates égales
                    return False
class Infection :
    """
    Un noeud de la liste Epidemie, contenant une date et un nombre d'infections.
    __precedent est la référence vers le noeud suivant (nombre d'infections a
    une date précédente) dans la liste.
    """
    def __init__(self,date,infections) :
        """
        @pre:  `date` est une instance de la classe Date.
               `infections` est un entier représentant le nombre d'infections
               à cette date.
        @post: Cet objet  a été initialisé
               avec les valeurs indiquées pour la date et le nombre d'infections
               et __precedent == None
        """
        self.__date = date
        self.__infections = infections
        self.__precedent = None

    def infections(self) :
        return self.__infections

    def set_precedent(self,infection) :
        self.__precedent = infection

    def precedent(self) :
        return self.__precedent

    def date(self) :
        return self.__date

    def __str__(self) :
        """
        @post: Retourne un string représentant cet objet, par exemple:
               "01.04.2020 : 25 infections"
        """
        return str(self.date()) + " : " + str(self.infections()) + " infections"
class Epidemie :
    """
    Une liste de données d'infections journalières, sous la forme
    d'une liste chainée d’Infection, ordonnées par date,
    en commençant par la plus récente.
    __premier est une reference vers la liste chaînée d'Infection,
    None si la liste est vide.
    """
    def __init__(self) :
        """
        @pre:  -
        @post: Cet objet a été initialisé pour une liste vide.
        """
        self.__premier = None   # premier noeud de la liste
        self.taille = 0       # nombre de noeuds de la liste

    def ajoute_infections(self, date, nombre) :
        """
        @pre:  `date` est la date du relevé.
               `nombre` est le nombre d'infections.
        @post: Le nouveau relevé  a été ajoutée dans liste, en respectant
               l'ordre des dates. La taille de la liste a été mise à jour.
        """
        if self.taille==0:
            self.__premier=Infection(date,nombre)
            self.taille+=1
        else:
            if Date.before(self)<self.date():
                self.__premier=Infection(self.date(),nombre)
            else:
                self.__premier=Infection(self.date(),nombre)
            
    def moyenne(self) :
        """
        @pre:  -
        @post: retourne None si la liste est vide,
               sinon, retourne la moyenne des infections journalières
               sur toute la liste.
        """
        

    def __str__(self) :
        """
        @pre: -
        @post: retourne un string représentant la liste.
        """
        return str(self.__premier.date()) + " : " +  str(self.__premier.infections())+ " infections"
    
    
def spambot(filename):
    """
    @pre: `filename` est une chaîne de caractères.
    @post: si `filename` est le nom d'un fichier contenant du texte, où le texte
    est constitué de mots séparés par des espaces ou des nouvelles lignes,
    la fonction cherche dans ce fichier la première occurence d'un mot qui
    est une adresse mail dans le format

    prenom.nom@domaine.extension

    où `prenom`, `nom`, `domaine` et `extension` ne contiennent ni espace " ",
    ni le caractère "." ou "@".  Retourne [ `prenom`, `nom`, `domaine`,
    `extension` ] si une adresse mail est trouvée, une liste vide ([]) sinon.

    En cas d'erreur d'entrée-sortie à la lecture, ou si le fichier est vide,
    retourne la liste vide également.
    """
    try:
        with open(filename,"r") as file:
            liste=file.read().split()
            for i in liste:
                if '@' in i:
                    l=i.split("@")
                    break
            if l!=[]:
                spam=[]
                for i in range(len(l)):
                    for j in range(len(l[i])):
                        if l[i][j]==".":
                            spam.append(l[i][:j])
                            spam.append(l[i][j+1:])
                return spam
            else:
                return []
    except:
        return []
    


def carremagique(carre):
    l=[]
    ligne=len(carre)
    col=len(carre[0])
    val=sum(carre[0])
    if ligne==col:
        #Pour les lignes
        for i in range(ligne):
            somme=0
            for j in range(col):
                somme+=carre[i][j]
            if somme!=val:#Condition permettant d'arreter l'execution si une ligne n'est pas egale a val(somme de la 1ere ligne)
                return False
            else:
                l.append(somme)
        #Pour les colonnes:
        i,j=0,0
        for i in range(ligne):
            somme=0
            for j in range(col):
                somme+=carre[i][j]
            if somme!=val:#Condition permettant d'arreter l'execution si une colonne n'est pas egale a val(somme de la 1ere ligne)
                return False
            else:
                l.append(somme)
        #Pour les diagonales
        j=-1
        somme,sommes=0,0
        for i in range(ligne):
            somme+=carre[i][i]
            sommes+=carre[i][j]
            j+=-1
        if somme!=val or sommes!=val:#Condition permettant d'arreter l'execution si une diagonale n'est pas egale a val(somme de la 1ere ligne)
            return False
        else:
            l.append(somme)
            l.append(sommes)
        
        #Verifier que toutes les valeurs sont les mêmes
        for i in range(len(l)-1):
            if l[i]!=l[i+1]:
                return False
        return l[0]
    else:
        return False
   
   

if __name__ == '__main__':
    print("----Calembour----")
    print(calembour('lambada','badaboum'))   # lambadaboum
    print(calembour('lambada','boumbam'))   # lambadaboumbam
    print(calembour('info','sinf')) # infosinf
    print(calembour('sinf','info')) # sinfo
    print(calembour('baboubaboum','baboumdou')) 
    print()
    print("----Occurrences----")
    print(occurrences("je chasse les poules les hommes me chassent toutes les poules se ressemblent et tous les hommes se ressemblent"))
    print(occurrences("je chasse les poules les gens  je suis trop content oui content"))
    print()
    print("------ClasseEpidemie------")
    print("----Classe Date----")
    d=Date(2020,12,1)
    other_date=Date(2020,12,2)
    print(d.__str__())
    print(d.before(other_date))
    print("----Classe Infections----")
    date=Date(2000,12,3)
    i=Infection(date,25)
    print(i.infections())
    i.set_precedent(234)
    print(i.precedent())
    print(i.date())
    print(i)
    print("----Classe Epidemie----")
    covid=Epidemie()
    date=Date(2011,5,12)
    print()
    print("----Spambot----")
    print(spambot("spam.txt"))
    print()
    print("----CarreMagique----")
    print(carremagique([ [ 1, 2 ], [ 2, 1 ] ]))  # retourne False
    print(carremagique([ [ 2, 7, 6 ], [ 9, 5, 1 ], [ 4, 3, 8 ] ]))  # retourne 15

    

