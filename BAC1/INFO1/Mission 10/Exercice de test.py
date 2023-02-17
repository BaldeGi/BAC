import math
import unittest
def carre_parfait (x) :
    '''
    retourne true si l'entier en argument est un carré parfait, false sinon
    '''
    if x<0: return False
    root=math.sqrt(x)
    return root.is_integer()
        
        

class MyClassTest(unittest.TestCase) :
    
    def setUp(self):
        """Initialisation des tests."""
        self.l = [4,9,16]
        self.lst=[3,5,7]
        self.neg=[-2,-4]
    
    def test_carre(self):
        
        for x in self.l:
            self.assertEqual(carre_parfait(x),True)
            
    def test_carre2(self):
        
        for x in self.lst:
            self.assertEqual(carre_parfait(x),False)
            
    def test_carre3(self):
        
        for x in self.neg:
            self.assertEqual(carre_parfait(x),False)

if __name__ == '__main__':
    unittest.main()