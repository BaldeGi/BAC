def prs_eq(a,b):
    return abs(a-b)<=0.001

def serie(n):
    sum =0
    if n==0 : return 0
    for i in range(1,n+1):
        sum+=((-1)**i)/(2*i-1)
    return sum
    
    
def trouve(val):
    i = 0
    while not prs_eq(serie(i),val):
        i+=1
    return serie(i)

def moyenne_mobile(lst,n):
    l=[]
    for i in range(len(lst)):
        if i<n:
           l.append(sum(lst[:i+1])/len(lst[:i+1]))
        else: l.append(sum(lst[(i+1)-n:i+1])/n)
    return l







class Matrice :
   

    def __init__(self,m,n) :
        """
        pre: m ≥ 0, n ≥ 0
        post: Initialise une matrice de dimension m x n dont toutes les valeurs sont égales à 0.0
              La variable self.repr contient la représentation.
              Les variables self.m et self.n contiennent, respectivement, les dimensions
              m et n de la matrice.
        """
        self.m = m
        self.n = n
        rep= []
        for i in range(self.m):
            l =[]
            for j in range(self.n):
                l.append(0.0)
            rep.append(l)
        self.rep = rep
        
        
            
    
        
        
        
                
        

    def lignes(self) :
        """
        pre:  /
        post: retourne le nombre de lignes m de cette matrice
        """
        return self.m
        # A COMPLETER

    def colonnes(self) :
        """
        pre:  /
        post: retourne le nombre de colonnes n de cette matrice
        """
        return self.n
        # A COMPLETER

    def get(self,r,c) :
        """
        pre:  1 <= r <= m
              1 <= c <= n
        post: retourne la valeur de la cellule de la matrice à la ligne r et à la colonne c,
              ou 0.0 si aucune valeur n'a encore été attribuée à cette cellule
        """
        for i in range(self.m):
            for j in range(self.n):
                if i+1==r and j+1 == c:
                    return self.rep[i][j]
        return 0.0
            
        
        # A COMPLETER

    def set(self,r,c,val) :
        """
        pre:  1 <= r <= m
              1 <= c <= n
        post: assigne la valeur val à la cellule de la matrice
              à la ligne r et à la colonne c
        """
        for i in range(self.m):
            for j in range(self.n):
                 if i+1==r and j+1 == c:
                     self.rep[i][j]=val
        
        
                
        # A COMPLETER

    def __eq__(self,autre) :
        """
        pre:  /
        post: retourne True si autre est une instance de Matrice de mêmes dimensions et contenant
              les mêmes valeurs que cette matrice, False sinon
        """
        if isinstance(autre,Matrice):
            if self.lignes()==autre.lignes() and self.colonnes() == autre.colonnes():
                for i in range(len(self.rep)):
                    for j in range(len(self.rep[i])):
                        if self.rep[i][j]!= autre.rep[i][j]:
                            return False
                return True
        # A COMPLETER
        
    def repr(self):
        d ={}
        for i in range(len(self.rep)):
            l ={}
            for j in range(len(self.rep[i])):
                if self.rep[i][j]!=0.0:
                    l[j+1] = self.rep[i][j]
                    d[i+1] = l
        return d
    
    
    
    
            
            
        
            
    
    

if __name__ == '__main__':
    print(serie(0))
    print(serie(1))
    print(serie(100))
    print()
    print(trouve(-0.666))
    print(trouve(-0.783))
    print()
    print(moyenne_mobile([0,1,2,3],2)) #[0.0,0.5,1.5,2.5]
    print(moyenne_mobile([0,1,2,3],3)) #[0.0,0.5,1.0,2.0]
    print()
    print()
    matrice = Matrice (2, 3)
    matrice.set(1, 1, 2.0)
    matrice.set(1, 3, 3.0)
    matrice.set(2, 1, 4.0)
    matrice.set(1, 1, 0.0)
    print(matrice.rep)
    print(matrice.get(1, 1))  # 0.0
    print(matrice.get(1, 3))  # 3.0
    print(matrice.repr()) #  {1: {3: 3.0}, 2: {1: 4.0}} ou {1: {1: 0.0, 3: 3.0}, 2: {1: 4.0}}
    print()
    matrice1 = Matrice (2, 3)
    matrice1.set(1, 2, 2.0)
    matrice1.set(1, 3, 3.0)
    matrice1.set(2, 1, 4.0)
    matrice1.set(1, 1, 0.0)
    print(matrice1.repr())
    print(matrice1.rep)
    print(matrice.__eq__(matrice1))
    print()
   
    
    
    
