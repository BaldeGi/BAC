class OrderedPair:
    '''
    Représente une paire de deux entiers (représenté en interne par une instance p de la classe Pair).
    Cette paire est considérée comme ordonnée si l'attribut a de p est plus petit ou égal à son attribut b
    '''

    def __init__(self):
        self.p = Pair(0, 0)
        self.ordered = True

    def set_a(self, n_a):
        """
        @pre -
        @post donne au premier élément de la paire la nouvelle valeur n_a
        """
        # À implémenter
        self.p=Pair(n_a,self.p.b)
        if (n_a<=self.p.b):
            self.ordered=True
        else:
            self.ordered=False

    def set_b(self, n_b):
        """
        @pre -
        @post donne au second élément de la paire la nouvelle valeur n_b
        """
        # À implémenter
        self.p=Pair(self.p.a,n_b)
        if (self.p.a<=n_b):
            self.ordered=True
        else:
            self.ordered=False
      




