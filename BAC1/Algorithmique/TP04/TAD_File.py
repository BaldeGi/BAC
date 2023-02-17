class Queue: 
    def __init__(self):
        """
        pre: - 
        post: crée une file vide
        """
        self.tab=[]
        self.length=0
    def __len__(self):
        """
        pre: -
        post: return la longueur de la file
        """
        return self.length
    def enqueue(self, item):
        """
        pre:-
        post: Ajouter un élément au début de la file
        """
        self.tab.append(item)
        self.length+=1
    def dequeue(self):
        """
        pre: len de la file doit être superieur ou égale à 1 
        post: Supprimer le premier élément de la file et renvoyez-le
        """
        val=self.tab[0]  
        del self.tab[0]   # ou self.tab.pop(0)
        self.length-=1
        return val
    def is_empty(self):
        """
        pre: -
        post: - Return True si la file est vide et false sinon
        """
        return self.tab==[]
    # Si vous le désirez, vous pouvez implémenter la méthode
    # __str__(self) pour obtenir une représentation de votre
    # file sous forme de string
    # Exemple:
    def __str__(self):
        str_queue = "This is a Queue. Ideally, I should report "\
        "my content.\n"
        return str_queue


#Exemples de tests:
file = Queue()
items = [i for i in range(1, 50)]

if not file.is_empty():
    print("Une nouvelle file devrait être vide après initialisation.")

for item in items:
    file.enqueue(item)
    if not len(file) == item:
        print("La taille de la file ({}) est incorrecte après ajout de l'élément : {}.".format(len(file), item))

for item in items:
    if not file.dequeue() == item:
        print("La suppression d'un élément ne renvoit pas le bon élément : {}.".format(item))




