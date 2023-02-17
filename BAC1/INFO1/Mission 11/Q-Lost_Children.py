class Child:
    """
    Vous devez vérifier si chaque enfant est là.
    Pour cela, vous avez accès au premier enfant avec la variable first_child (instance de la classe Child).
    La classe Child a la fonction is_next_valid pour vérifier si il a son camarade,
    et la fonction next_child pour avoir son camarade.
    """
    def is_next_valid():
        pass
        #retourne un booléen
    def next_child() :
        pass
        #retourne un Child
    
    #Qu'on devait implémentersur inginious
    def is_every_child_here(first_child):
        child = first_child
        while child.next_child() != first_child:
            if not child.is_next_valid():
                return False
            child = child.next_child()
        return True
