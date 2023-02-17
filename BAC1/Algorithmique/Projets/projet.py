from Methodes_utilitaires_projet import*
#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
Ce module contient les classes et fonctions de bases qui vous seront nÃ©cessaires
lors de la rÃ©alisation projet du cours d'algorithmique.
En particulier, ce module dÃ©clare:
  * La classe abstraite `ArbreBinaire` que vous devez complÃ©ter.
  * La fonction `creer_arbre(forme_parenthesee)` que vous devez implementer.
'''

class ArbreBinaire:
    '''
    Ce prototype de classe (Ã  modifier par vous) est une version simplifiÃ©e de 
    la classe qui vous a Ã©tÃ© prÃ©sentÃ© lors du cours sur l'implÃ©mentation des 
    arbres binaires.

    .. important::
       Le nom de la methode `simplifier` ainsi que sa signature vous
       sont imposÃ©s. Si vous modifiez un de ces Ã©lÃ©ments, votre code ne pourra
       pas Ãªtre validÃ©.
    '''

    def __init__(self, elem=None, left=None, right=None):
        '''
        :pre: -
        :post: initialize a new Binary Tree with "elem" stored at the root node,
               when "elem" is None, this is interpreted as an empty BinaryTree.
        '''
        self.root_elem  = elem  # An element at the root
        self.left_tree  = left
        self.right_tree = right
    
    def est_une_feuille(self):
        '''
        Renvoie `True` si et seulement si l'arbre considÃ©rÃ© est une feuille.

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie `True` ssi ce (sous-)arbre est une feuille.
        '''
        # TODO: C'est vous qui devez fournir une implÃ©mentation de cette mÃ©thode
        return self.left_tree is None and self.right_tree is None

    def a_un_enfant_gauche(self):
        '''
        Renvoie `True` si et seulement si l'arbre considÃ©rÃ© possÃ¨de un 
        sous-arbre Ã  gauche.

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie `True` ssi le sous arbre gauche de cet arbre existe
        '''
        # TODO: C'est vous qui devez fournir une implÃ©mentation de cette mÃ©thode
        return self.left_tree == None

    def a_un_enfant_droit(self):
        '''
        Renvoie `True` si et seulement si l'arbre considÃ©rÃ© possÃ¨de un 
        sous-arbre Ã  droite.

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie `True` ssi le sous arbre droit de cet arbre existe
        '''
        # TODO: C'est vous qui devez fournir une implÃ©mentation de cette mÃ©thode
        return self.right_tree
    
    
    
    def hauteur(self):
        '''
        Renvoie le nombre de niveaux maximum en dessous du noeud courant. 
        (Note: pour une feuille, ca sera toujours 0).

        Suggestion, afin de rendre votre implÃ©mentation plus efficace, vous 
        pourriez vouloir stocker le rÃ©sultat de cette methode dans un attribut
        privÃ© de votre classe et le renvoyer chaque fois que cette mÃ©thode est
        appelÃ©e. Quel impact cela a-t-il sur la complexitÃ© spatiale de votre 
        algorithme ? Et sur la complexitÃ© temporelle ? 
        (A discuter avec l'assistant lors de la sÃ©ance de follow-up)

        :pre:   L'arbre est valide (il a pu Ãªtre interpÃ©tÃ© correctement)
        :post:  Renvoie Renvoie le nombre de niveaux maximum en dessous du noeud 
                courant. 
        '''
        # TODO: C'est vous qui devez fournir une implÃ©mentation de cette mÃ©thode
        res = 0
        if self.est_une_feuille():
            return res
        return 1 + max(self.left_tree.hauteur() , self.right_tree.hauteur())
    
    def poids(self):
        res = 0
        if self.est_une_feuille():
            return res
        elif self.left_tree is None and  self.right_tree is not None :
            return 1+ self.right_tree.poids()
        elif self.left_tree is not None and  self.right_tree is None :
            return 1+ self.left_tree.poids()
        return 1 + (self.left_tree.poids() + self.right_tree.poids())
    
    #Fais pas partie du projet
    def taille(self):
        res = 0
        if self.est_une_feuille():
            return res
        return 1 + (self.left_tree.taille() + self.right_tree.taille())

       

    def simplifier(self, i):
        '''
        Renvoie un dÃ©coupage de la phrase correspondant au `i`eme niveau de
        l'arbre d'analyse.

        :pre:    L'arbre est valide (il a pu Ãªtre interprÃ©tÃ© correctement)
        :post:   Renvoie une chaine de caractere reprÃ©sentant le dÃ©coupage de
                 l'arbre selon son `i` eme niveau.
        '''
        # TODO: C'est vous qui devez fournir une implÃ©mentation de cette mÃ©thode
    
        def infixe(self,i,l=""):
            if i==0:
                if self.est_une_feuille():
                    return self.root_elem
                return l+infixe(self.left_tree,i)+" "+infixe(self.right_tree,i)
            else:
                s=i
                if self.est_une_feuille():
                    return self.root_elem
                if i==s:
                    return l+infixe(self.left_tree,i-1)+"|"+infixe(self.right_tree,i-1)
        return infixe(self,i)
    
    
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    #Fais pas partie du projet , juste pour tester
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_tree is None and self.left_tree is None:
            line = '%s' % self.root_elem
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_tree is None:
            lines, n, p, x = self.left_tree._display_aux()
            s = '%s' % self.root_elem
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_tree is None:
            lines, n, p, x = self.right_tree._display_aux()
            s = '%s' % self.root_elem
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_tree._display_aux()
        right, m, q, y = self.right_tree._display_aux()
        s = '%s' % self.root_elem
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
                     '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
                      (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        
    
    
            

def creer_arbre(forme_parenthesee):
    '''
     Cette fonction permet de crÃ©er une instance d'ArbreBinaire correspondant Ã  
     l'arbre encodÃ©e dans la chaine de caractÃ¨res en forme parenthÃ©sÃ©e.

     :pre:  Le paramÃ¨tre forme_parenthesee est une chaine de caractÃ¨res qui 
            encode un arbre d'analyse valide.
     :post: Renvoie une instance de la classe ArbreBinaire ci-dessus.
            L'instance retournee correspond Ã  ce qui est encodÃ© dans forme_parenthesee.

     :exc:  Si la prÃ©condition devait Ãªtre violÃ©e lors de l'appel Ã  cette fonction,
            vous Ãªtes autorisÃ©s Ã  lever une exception de type ValueError qui est une
            exception standard du langage Python3.
    '''
    # TODO: A vous d'implÃ©menter cette fonction
    return creer_arbre_aux(valid_list(forme_parenthesee))
    
if __name__ == '__main__':
    '''
     Ce simple test a pour but de vous permettre de valider plus facilement le rÃ©sultat de votre
     travail. Ce point d'entrÃ©e **ne sera en aucun cas appelÃ©e** lors de l'Ã©valuation de votre
     travail sur INGInious. Il est donc nÃ©cessaire que vous Ã©criviez votre code en respectant les
     instructions qui vous sont donnÃ©es ci-dessus.

     Pour aller plus loin (Optionnel):
     ---------------------------------
     Ceux qui veulent effectuer une vÃ©rification plus robuste de leur solution sont invitÃ©s Ã 
     Ã©crire une suite de tests avec le module `unittest` (ou `nose`) de python. Celle-ci vous
     permettra de valider le comportement des/de l' implÃ©mentation(s) de la classe `ArbreBinaire`
     que vous avez rÃ©alisÃ© ainsi que celui de la mÃ©thode 'creer_arbre()' dÃ©finie ci-dessus.
    '''
    # Une phrase d'exemple
    exemple = '''
              ((((2 An Welcome) ((4 engaging Bonjour 42 ça va ?) (2 overview))) ((2 of) (((2 Johnson) (2 's)) ((2 eccentric) (3 career))))) (2 .))
              '''

    # CrÃ©ation d'un arbre d'analyse correspondant Ã  l'exemple donnÃ© ci-dessus.
    arbre = creer_arbre(exemple)
    # Calcul du dÃ©coupage de l'arbre selon le niveau 1
    calcule=arbre.simplifier(1)
    attendu="An engaging overview of Johnson 's eccentric career|."

    # TODO: A vous de jouer.
    #       Cet exemple de programme imprime le decoupage pour l'exemple donnÃ© dans
    #       les instructions du projet. Vous Ãªtes encouragÃ©s Ã  dÃ©finir de nouveaux
    #       tests par vous mÃªme ou adapter cet exemple de programme.
    print("Le decoupage calculÃ© est '{}'.".format(calcule))
    print("Le decoupage attendu est '{}'.".format(attendu))
    
    tree2 = ArbreBinaire(None,ArbreBinaire(None,ArbreBinaire(None, ArbreBinaire("An"),
    ArbreBinaire(None, ArbreBinaire("engaging"), ArbreBinaire("overview"))),
    ArbreBinaire(None,ArbreBinaire("of"),
    ArbreBinaire(None, ArbreBinaire(None,ArbreBinaire("Johnson"),
    ArbreBinaire("'s")), ArbreBinaire(None,ArbreBinaire("eccentric"),
    ArbreBinaire("career"))))),ArbreBinaire("."))
    
    print("--------------------")
    print(tree2.a_un_enfant_gauche())
    
    
    print(arbre.hauteur())
    print(arbre.taille())
    print("\n")
   
    print("\n")
    print(arbre.simplifier(0))
    print(arbre.simplifier(1))
    print(arbre.simplifier(2))
    print(arbre.simplifier(3))
    print(arbre.simplifier(4))
    print(arbre.display())
    
    print(tree2.poids())
    
   
    
    
    
    
   
    
    