class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __eq__ (self, p):
        """
        @pre    -
        @post   Retourne true si la paire p est égale à l'objet.
                Retourne false sinon
        """
        if (self.a,self.b)==p:
            return True
        return False
q=Pair(1,2)
p=Pair(1,2)
print(q.__eq__(p))
p=Pair(1,3)
print(p==q)