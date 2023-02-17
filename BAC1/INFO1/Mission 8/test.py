from mission8 import Duree, Chanson, Album

# TEST DE LA METHODE __str__ DE LA CLASSE Duree

def test_Duree_str(duree1) :
    duree0=Duree(12,45,30)
    assert duree0.__str__() == "12:45:30", "Test 1 Duree __str__"
    assert duree1.__str__() == "10:20:59", "Test 2 Duree __str__" 
d1 = Duree(10,20,59)
test_Duree_str(d1)
    
# TEST DE LA METHODE toSecondes DE LA CLASSE Duree

def test_Duree_to_secondes(duree1,duree2,duree3) :
    assert duree1.to_secondes() == 37259, "Test 1 Duree toSecondes"
    assert duree2.to_secondes() == 31285, "Test 2 Duree toSecondes"
    assert duree3.to_secondes() == 119 , "Test 3 Duree toSecondes"
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)
d3 = Duree( 0,1,59)
test_Duree_to_secondes(d1,d2,d3) 
    

# TEST DE LA METHODE delta DE LA CLASSE Duree

def test_Duree_delta(duree1,duree2,duree3,duree4):
    assert duree1.delta(duree2) == 5974, "Test 1 Duree delta"
    assert duree3.delta(duree4) == 0, "Test 2 Duree delta"
    
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)
d3 = Duree(0,1,0)
d4 = Duree(0,1,0)
test_Duree_delta(d1,d2,d3,d4)

# TEST DE LA METHODE apres DE LA CLASSE Duree

def test_Duree_apres(duree1,duree2):
    duree0 = Duree(0,0,0)
    assert duree1.apres(duree2),      "Test 1 Duree apres"
    assert not duree0.apres(duree1),  "Test 2 Duree apres"
d1 = Duree(10,20,59)
d2 = Duree( 8,41,25)
test_Duree_apres(d1,d2)    
# TEST DE LA METHODE ajouter DE LA CLASSE Duree

#def test_Duree_ajouter(duree1,duree2,duree3,duree4):
    #d1 = Duree(10,20,59)
    #assert duree1.ajouter(duree2)==(19, 2, 24), "Test 1 Duree ajouter"
    #assert duree3.ajouter(duree4)==(1, 43, 34), "Test 2 Duree ajouter"

#d2 = Duree( 8,41,25)
##d3 = Duree(1,20,9)
#d4 = Duree(0,23,25) 
#test_Duree_ajouter(d1,d2,d3,d4)



################################
# Tests pour la classe Chanson #
################################

# TEST DE LA METHODE __str__ DE LA CLASSE Chanson

def test_Chanson_str(chanson,chanson2) :
    assert chanson.__str__()=="Let's Dance - David Bowie - 00:04:05"
    assert chanson2.__str__()=="Let's go - David - 01:04:05"  
chanson = Chanson("Let's Dance", "David Bowie", Duree(0,4,5))
chanson2 = Chanson("Let's go", "David", Duree(1,4,5))
test_Chanson_str(chanson,chanson2)



##############################
# Tests pour la classe Album #
##############################

# TEST DE LA METHODE __str__ DE LA CLASSE Album
def test_Album_str(chanson,chansons):
    assert alb.__str__()=="Album 1 (2 chansons , 00:14:10)\n01: Let's Dance - David Bowie - 00:04:05\n02: Let's go - David Bowie - 00:10:05"
                        
                           
alb=Album(1)
chanson=(Chanson("Let's Dance", "David Bowie", Duree(0,4,5)))
chansons=(Chanson("Let's go", "David Bowie", Duree(0,10,5)))
alb.add(chanson)
alb.add(chansons)
test_Album_str(chanson,chansons)

# TEST DE LA METHODE add DE LA CLASSE Album
def test_Album_add(chanson,chansons):
    assert(alb.add(chanson))==True
    assert (alb.add(chansons))==False
    
alb=Album(1)
chanson=Chanson("Let's Dance", "David Bowie", Duree(0,4,5))
chansons=Chanson("Let's Dance", "David Bowie", Duree(1,40,5))
test_Album_add(chanson,chansons)


