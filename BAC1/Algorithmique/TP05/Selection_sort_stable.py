#!/usr/bin/python3

class book():
    '''
    Classe représentant un livre, correspondant à une paire nom-année d'édition
    '''
    def __init__(self, name, year):
        '''Constructuer de la classe Book'''
        self.name = name
        self.year = year

    def __lt__(self, other):
        '''Permet de comparer deux éléments. Correspond à l'opérateur <'''
        if isinstance(other, book): #Test si l'autre élément est également un objet de type book
            return self.year < other.year #Si c'est le cas, renvoie le résultat de la comparaison des dates d'edition
        else:
            return NotImplemented #Sinon, indique que la comparaison n'est pas implémentée
    
    def __le__(self, other):
        '''Permet de comparer deux éléments. Correspond à l'opérateur <='''
        if isinstance(other, book):
            return self.year <= other.year
        else:
            return NotImplemented

    def __eq__(self, other):
        '''Permet de comparer deux éléments. Correspond à l'opérateur =='''
        if isinstance(other, book):
            return self.year == other.year
        else:
            return NotImplemented

    def __str__(self):
        return '{date}: {name}'.format(date=self.year, name=self.name)



def selection_sort_stable(books):
    """
    pre: `books` est un tableau (list) de `book`
    post: tri par sélection STABLE du tableau passé en paramètre.
        Les éléments sont triés en place
    """
    for i in range(len(books)-1):
        minimum = books[i]
        for j in range(i+1,len(books)):
            if books[j] < minimum :
                minimum = books[j]
                index=j
        if books[i]!= minimum:
            books.insert(i,minimum)
            del books[index+1]
        
    
    for i in books:
        print(i)


############
#Exemple de test:

#Crée une liste de livres


#Trie en place les libres de la bibliothèque
print(selection_sort_stable([
            book("1) L'incroyable Histoire 0", 2020),
            book("2) L'incroyable Histoire 0 (reéd. 1)", 2021),
            book("3) L'incroyable Histoire 0 (reéd. 2)", 2022),
            book("4) L'incroyable Histoire 1", 2021),
            book("5) L'incroyable Histoire 1 (reéd. 1)", 2022),
            book("6) L'incroyable Histoire 1 (reéd. 2)", 2023),
            book("7) L'incroyable Histoire 1 (reéd. 3)", 2024),
            book("8)  L'incroyable Histoire 2", 2022),
            book("9) L'incroyable Histoire 2 (reéd. 1)", 2023),
            book("10) L'incroyable Histoire 2 (reéd. 2)", 2024),
            book("11) L'incroyable Histoire 2 (reéd. 3)", 2023)
            ]))






