from assistant import*
def testfile():
    commande=(input("Entrez le nom du fichier pour l'ouvrir : "))
    try:
        file(commande)
    except:
        print("Fichier inexistant ou vide")
testfile()
def test_info():
    filename=input("Entrez le fichier pour le teste du nombre de lignes et carateres: ")
    if filename=="filename.txt":
        ass=(str(4) + " lignes " + str(19) + " caractères")
        assert info(filename)==ass
    elif filename=="done.txt":
        ass1=(str(5) + " lignes " + str(53) + " caractères")
        assert info(filename)==ass1
    elif filename=="filename_in.txt":
        ass2=(str(4) + " lignes " + str(26) + " caractères")
        assert info(filename)==ass2
    else:
        print("Nom de fichier incorrect ou ne se trouvant pas parmis les tests")
test_info()

def test_search():
    filename=input("Entrez le fichier pour le teste cherchant le mot dans le dictionnaire: ")
    assert search(filename,"pye")==True
    assert search(filename,"odalisque")==True
    assert search(filename,"odique")==False
test_search()


def test_somme():
    valeurs=input("Entrez la suite de nombres dont vous voulez calculer la somme : ")
    try:
        somme(valeurs)
    except ValueError:
        print("ValueError")
test_somme()

def test_somme():
    assert somme(input("Entrez une suite de nombre dont la somme est egale à 15 ou pas  :" ))==15
    assert somme(input("Entrez une suite de nombre dont la somme est egale à 40 ou pas  :" ))==40
    assert somme(input("Entrez une suite de nombre dont la somme est egale à 3 ou pas  :" ))==3
    assert somme(input("Entrez une suite de nombre dont la somme est egale à 18 ou pas  :" ))==18
test_somme()

def test_avg():
    assert avg(input("Entrez une suite de nombre dont la moyenne est egale à 3 ou pas : " ))==3.0
    assert avg(input("Entrez une suite de nombre dont la moyenne est egale à 5 ou pas : " ))==5
    assert avg(input("Entrez une suite de nombre dont la moyenne est egale à 30 ou pas : " ))==30
    assert avg(input("Entrez une suite de nombre dont la moyenne est egale à 25 ou pas : " ))==25
test_avg()

def test_avg():
    valeurs=input("Entrez la suite de nombres dont vous voulez calculer la moyenne : ")
    try:
        avg(valeurs)
    except ValueError:
        print("ValueError")
test_avg()




