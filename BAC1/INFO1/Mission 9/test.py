from mission9 import Article, Facture, ArticleReparation,Piece,ArticlePiece

class TestArticleEtape1 :

    articles=[ArticleReparation(0.75),ArticleReparation(1.65),ArticleReparation(2.0),ArticleReparation(0.45)]
    
    @classmethod
    def run(cls) :
        for art in cls.articles :
            print(art)

class TestFactureEtape1 :
    
    @classmethod
    def run(cls) :
        facture = Facture("PC Store - 22 novembre", TestArticleEtape1.articles)
        print(facture)
        
class TestArticleEtape3 :

    articles = [ Article("laptop 15\" 8GB RAM", 743.79),
                 Article("installation windows", 66.11),
                 Article("installation wifi", 45.22),
                 Article("carte graphique", 119.49)
                 ]
    
    articles2 = [ Article("top 15\" 8GB RAM", 743.79),
                 Article("windows", 66.11),
                 Article("wifi", 45.22),
                 Article("carte graphique", 119.49)
                 ]
    
    @classmethod
    def run(cls) :
        for art in cls.articles :
            print(art)
        print()
        print("*** TEST DE LA CLASSE ArticlePiece 2 ***")
        print()
        for art in cls.articles2 :
            print(art)

    
class TestFactureEtape3:
    piece1=Piece("disque dur 350 GB",49.99,0,True,False)
    piece2=Piece("souris bluetooth",15.99,0,True,False)
    piece3=Piece("adaptateur DVI - VGA",12.00,0,True,False)
    piece4=Piece("Java in a Nutshell",24.00,0,True,False)
    piece5=Piece("souris bluetooth",15.99,0,True,False)
    
    piece0=Piece("disque dur 350 GB",49.99,0,True,False)
    piece=Piece("bluetooth",15.99,0,True,False)
    
    articles=[ArticlePiece(1,piece1),ArticlePiece(3,piece2),ArticlePiece(5,piece3),ArticlePiece(2,piece4),ArticlePiece(5,piece5)]
    articles2=[ArticlePiece(1,piece0),ArticlePiece(3,piece)]

    facture = Facture("No {} PC Store - 22 novembre".format(Facture.numero), TestArticleEtape3.articles)
    facture2 = Facture("No {} PC Store - 22 novembre".format(Facture.numero), TestArticleEtape3.articles2)
    @classmethod
    def run(cls):
        for i in cls.articles:
            TestArticleEtape3.articles.append(i)
        print(cls.facture)
        for j in cls.articles2:
            TestArticleEtape3.articles2.append(j)
        print(cls.facture2)

class TestPrintLivraison:
    piece0=Piece("disque dur 350 GB",49.99,0,True,False)
    art=[ArticlePiece(1,piece0)]
    facture = Facture("No {} PC Store - 22 novembre".format(Facture.numero), TestArticleEtape3.articles)
    factures=facture.livraison_str()
    @classmethod
    def run(cls) :
        print(cls.factures)
if __name__ == "__main__":

    print("*** TEST DE LA CLASSE ArticleReparation ***")
    print()
    TestArticleEtape1.run()

    print()
    print("*** TEST DE LA CLASSE Facture pour la class ArticleReparartion ***")
    print()
    TestFactureEtape1.run()
    
    print("*** TEST DE LA CLASSE ArticlePiece 1 ***")
    print()
    TestArticleEtape3.run()

    print()
    print("*** TEST DE LA CLASSE Facture pour la class ArticlePiece ***")
    print()
    TestFactureEtape3.run()
    
    print("*** TEST DE LA Methode PrintLivraion  ***")
    print()
    TestPrintLivraison.run()
    
    
    
    
    
