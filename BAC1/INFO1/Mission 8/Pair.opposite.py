class Pair:

    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def opposite(self):
        """
        @pre        -
        @post   retourne une nouvelle instance de Pair dont les deux
                éléments sont les opposés de ceux de cette paire-ci.
                L'instance appelante reste inchangée.
        """
         # À implémenter
        return Pair(-self.a,-self.b)

p=Pair(10,-2)
print(p)
p.a=12
print(p)
q=p.opposite()
print(p)
print(q)