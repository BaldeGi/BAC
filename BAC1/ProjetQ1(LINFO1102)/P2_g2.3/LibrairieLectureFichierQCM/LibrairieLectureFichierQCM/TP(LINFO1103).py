#Top3
#Retourner les indices des trois valeurs maximale
"""mesures=[10, 0, 5, 10, 30, 10, 20, 30]
l=[]
l1=list(mesures)
for j in range(3):
    a=(l1.index(max(l1)))
    l.append(a)
    l1[a]=min(l1)-1
print(l)"""

#Marché du pouvoir quotient d'hare(repartir les sieges pour les parties)
"""n_sieges=6
resultat_vote= [437,478,85]
allo_exact=[]
t=[]
pa_decimale=[]
sum=0
for i in (resultat_vote):
    sum+=i
    s=sum/n_sieges
for i in (resultat_vote):
    a_e=i/s
    allo_exact.append(a_e)
for i in (allo_exact):
    p_decimale=i%1
    pa_decimale.append(p_decimale)
    i=int(i)
    t.append(i)
som=0
for i in t:
    if som<n_sieges:
        m=pa_decimale.index(max(pa_decimale))
        t[m]+=1
        pa_decimale[m]=0 
        som=0
        for i in t:
            som+=i
print(t)"""

#Marché du pouvoir quotient d'hondt(repartir les sieges pour les parties)
"""allo_exact=[]
t=[]
pa_decimale=[]
t_i2=[]
t_myn=[]
sum=0
for i in (resultat_vote):
    sum+=i
    s=sum/n_sieges
for i in (resultat_vote):
    a_e=i/s
    allo_exact.append(a_e)
for i in (allo_exact):
    i=int(i)
    t.append(i)
    print(t)
    i2=i+1
    t_i2.append(i2)
for i in range (len(t_i2)):
    myn=resultat_vote[i]/t_i2[i]
    t_myn.append(myn)
    m=t_myn.index(max(t_myn))
som=0
for i in t:
    if som<n_sieges:
        m=t_myn.index(max(t_myn))
        t[m]+=1
        t_myn[m]=0
        som=0
        for i in t:
            som+=i
return t"""

#Retourner la paire de somme maximale
"""import math
n=[3, -9, -2, 6, 5, 2, -1, 5]
som_max= - math.inf
for i in range (len(n)-1):
    for j in range(i+1,len(n)):
        somme_courante= n[i]+n[j]
        if somme_courante>som_max:
            som_max=somme_courante
print(som_max)"""

#2
"""import math
n= [7, -10]
l=[]
som=0
for i in range(len(n)):
    l1=list(n)
for i in range(len(l1)):
    if len(l)<2:
        m=(l1.index(max(l1)))
        l.append(m)
        som+=l1[m]
        l1[m]= -math.inf
print(som)"""

"""import unittest
s="Amadou"
def occurence(s):
    s=s.upper()
    l=list(s)
    l1=[]
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
            print((l[i],l.count(l[i])))
occurence(s)
        
class test_occurence(unittest.TestCase):
    def test_occurence(self):
        self.assertEqual(occurence("AMADOU"),None)
    
if __name__=='__main__':
    unittest.main()"""

"""import unittest
n=11
def premier(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                premier=False
                return premier
                break
            else:
                premier=True
            return premier
    else:
        return None

premier(n)

class test_premier(unittest.TestCase):
    def test_premier(self):
        self.assertTrue(premier(7))
    def test_premier(self):
        self.assertIsNone(premier(1))
    def test_premier(self):
        self.assertEqual(premier(13),True)
    def test_premier(self):
        self.assertEqual(premier(28),False)
    
    
                               
if __name__=='__main__':
    unittest.main()"""
           
"""l=[]
n=12
def premier(n):
    premier=True
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    for i in range(2,sum):
        if sum%i==0:
            premier=False
            return premier
            break
        else:
            premier=True
        return premier
premier(n)
        
class test_premier(unittest.TestCase):
    def test_premier(self):
        self.assertTrue(premier(7))
    def test_premier(self):
        self.assertIsNone(premier(1))
    def test_premier(self):
        self.assertEqual(premier(13),True)
    def test_premier(self):
        self.assertEqual(premier(7),True)

if __name__=='__main__':
    unittest.main()"""

#Le quotient d'hondt
"""n_sieges=11
resultat_vote=[437,478,85]
allo_exact=[]
t=[]
pa_decimale=[]
t_i2=[]
t_myn=[]
sum=0
for i in (resultat_vote):
    sum+=i
    s=sum/n_sieges
for i in (resultat_vote):
    a_e=i/s
    allo_exact.append(a_e)
for i in (allo_exact):
    i=int(i)
    t.append(i)
    print(t)
    i2=i+1
    t_i2.append(i2)
    print(t_i2)
for i in range (len(t_i2)):
    myn=resultat_vote[i]/t_i2[i]
    t_myn.append(myn)
    print(t_myn)"""



#Ecrivez un code permettant de calculer la factorielle de n'importe quel nombre.
#Rappel : Factorielle de 0 et de 1 est égale à 1 dans les deux cas. Utilisez la recursion.
"""fact=1
n=-5
if n>=0:
    for i in range(1,n+1):
        if n==0 and n==1:
            print("1")
        else:
            fact*=i
    print(fact)
else:
    print("None")"""

#Trouver la valeur la plus grand de la liste et la retourner
#sans utiliser la fonction sort() et max()

"""l=[2,5,7,10,4]
max=l[0]
for i in range(1,len(l)-1):
    if l[i]>max:
        max=l[i]
print(max)"""

#Premier(Projet)
"""l=[]
def premier(n):
    for i in range(2,n):
        if n%i==0:
            l.append(i)
    if l!=[]:
        for i in range(len(l)):
            mi=min(l)
            ma=max(l)
            div=ma/mi
            if div==int:
                return div
                break
            else: 
                div=div//1
                return div
                break

    else:
        return -1"""

#Test
"""import unittest
from CorrPrime import*
class test_premier(unittest.TestCase):
    def test_premier(self):
        self.assertEqual(premier(14),3)
    def test_premier(self):
        self.assertEqual(premier(8),2)
    def test_premier(self):
        self.assertEqual(premier(7),None)
    
    
if __name__=='__main__':
    unittest.main()"""

#Test
"""import unittest
import sys

import Prime as student
import CorrPrime as correct

class test_premier(unittest.TestCase):
        
    def test_premier(self):
        args=14
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.premier(args)
        except Exception as e:
            self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.premier(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    
    def test_premier(self):
        args=8
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.premier(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.premier(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
    
    def test_premier(self):
        args=7
        rep = _("Votre fonction a retourné {} lorsqu'elle est appelée avec {} comme argument alors que la réponse attendue est {}")
        try:
            student_ans = student.premier(args)
        except Exception as e:
             self.fail("Votre fonction a provoqué l'exception {}: {} avec comme argument {}".format(type(e), e))
        correct_ans = correct.premier(args)
        self.assertEqual(student_ans, correct_ans,rep.format(student_ans, args, correct_ans))
        
    
if __name__=='__main__':
    unittest.main()"""
    
"""a=11
b=24
def divisor(a,b):
    l=[]
    l1=[]
    if a==b:
        print("ok")
    elif a>0 and b>0:
        for i in range(2,a):
            if a%i==0:
                l.append(i)
        for j in range(2,b):
            if b%j==0:
                l1.append(j)
        if len(l)>len(l1):
            print("ok")
        else: 
            print("ok")
    elif a<0 and b<0:
        print(-1)
    else:
        print([])
divisor(a,b)"""


"""l=[1, 5,5,7,7,7]
l1=[]
l2=[]
l3=[]
l4=[]
for i in range (len(l)):
    if l[i] not in l1:
        l1.append(l[i])
        l2.append(l.count(l[i]))
for i in range(len(l2)):
    if len(l2)>=2:
        som=0
        for i in range (len(l2)):
            print(l2)
            if l2[i]>=2:
                som+=1
                print(som)
                l3.append(l2[i])
                mode1=(min(l3[i]))"""






B=[[2.0,4.0,62.0]]
A=[[1.0],[4.0],[15.0]]
def multiply(A,B):
    l = [[1, 1, 1], 
   
            [1, 1, 1], 

            [1, 1, 1]]
    try:
        #Verifie si les deux matrices ont la même dimension
        if len(A)==len(B[0]):
            #Parcours les lignes de la première matrice
            for i in range(len(A)):
                #Parcours les colonnes de la deuxième matrice
                for j in range(len(B[0])):
                    for m in range(len(B)):
                        #Multiplie le nombre trouver par le produit de ce calcule ci-dessous par 1.
                        #ça fait ce produit pour chaque position i(ligne) et j (colonne)
                        l[i][j] *= A[i][m] * B[m][j]
            return l
        else:
            raise Exception('Dimension mismatch')
    except:
        return "La dimension des matrices ne sont pas égale"
    
multiply(A,B)







    
    
        
    
    
   