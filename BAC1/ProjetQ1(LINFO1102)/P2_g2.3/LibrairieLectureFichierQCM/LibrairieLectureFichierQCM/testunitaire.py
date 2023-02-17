import unittest
def approx_pi(i):       

    """@pre:   i est un entier tel que i >= 0
    @post:  retourne une estimation de pi en sommant
            les i + 1 premiers termes de la série de Gregory-Leibniz"""

    ### VOTRE REPONSE
    sum=0
    if i>=0:
        for n in range (i+1):
            sum+=4*((-1)**n/(2*n+1))
        return sum
    
class test(unittest.TestCase):
    def test_pi(self):
        self.assertEqual(approx_pi(0),4)
        self.assertEqual(approx_pi(1),2.666666666666667)
        self.assertEqual(approx_pi(2),3.466666666666667)
        self.assertEqual(approx_pi(3),2.8952380952380956)
        self.assertEqual(approx_pi(1000),3.1425916543395442)
                               
if __name__=='__main__':
    unittest.main()