
###############
### ARTICLE ###
###############

"""
    Cette classe reprÃ©sente un Article de facture simple,
    comprenant un descriptif et un prix.
"""
class Article :

    __taux_tva = 0.21   # TVA a 21%
    
    @classmethod
    def getTVA(cls):
        return cls.__taux_tva
    
    def __init__(self,d,p):
        """
        Cree un article avec description d et prix p.
        """
        self.__description = d
        self.__prix = p

    def description(self):
        """
        Retourne la description de cet article.
        """
        return self.__description
        
    def prix(self):
        """
        Retourne le prix (HTVA) de cet article.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        Retourne le taux de TVA (mÃªme valeur pour chaque article)
        """    
        return Article.getTVA()

    def tva(self):
        """
        Retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        Retourne le prix de larticle, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        Retourne un texte decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} euro HTVA".format(self.description(), self.prix())
    
    
#########################
### ArticleReparation ###
#########################
"""
    Cette classe représente une prestation de réparation
    de durée donnée (un float, en heures)
"""   
class ArticleReparation(Article):
    def __init__(self,duree):
        if type(duree)!=float:
            return
        else:
            self.__duree=duree
        
    def description(self):
        return "Reparation ({} heures)".format(self.__duree)
    
    def prix(self):
        return 20+self.__duree*35
    
    

###############
### PIECE   ###
###############   
    
class Piece:
    def __init__(self,description,prix_unit,poids_unit=0,fragile=False,tva_reduite=False):
        self.__poids_unit=poids_unit
        self.__fragile=fragile
        self.__tva_reduite=tva_reduite
        if type(description)==str:
            self.__description=description
        if type(prix_unit)==float:
            self.__prix_unit=prix_unit
        if type(description)!=str or type(prix_unit)!=float:
            return 
        
        
    def description(self):
        return self.__description
    
    def prix(self):
        return self.__prix_unit
    
    def poids(self):
        return self.__poids_unit
    
    def fragile(self):
        return self.__fragile
    
    def tva_reduit(self):
        return self.__tva_reduite
    
    def __eq__(self,other):
        return (self.__description,self.__prix_unit)==(other.__description,other.__prix_unit)
    

######################
### ArticlePiece   ###
############### ######
    
class ArticlePiece(Article):
    def __init__(self,nbre,pce):
        self.__nbre=nbre
        self.__pce=pce
        
    def get_nbre(self):
        return self.__nbre
    
    def get_pce(self):
        return self.__pce
    
    def description(self):
        return "{}*{} @ {}".format(self.get_nbre(),self.get_pce().description(),self.get_pce().prix())
    
    def prix(self):
        return self.__pce.prix()*self.__nbre
    
    def tva(self):
        tva=21/100
        if self.__pce.tva_reduit():
            tva=6/100
        return self.prix()*tva
    

###############
### FACTURE ###
###############


class Facture :
    
    numero=1

    def __init__(self, description, articles):
        """
        CrÃ©e une facture avec une description (titre) et une liste d'articles.
        @pre  description est un string court dÃ©crivant la facture
              articles est une liste d'objets de type Article
        @post Une facture avec une description (titre) et un liste d'articles a Ã©tÃ© crÃ©e.
        """
        self.__reference = description
        self.__articles = articles
        self.numero=Facture.numero
        Facture.numero+=1

    def description(self):
        """
        Retourne la description de cette facture.
        """
        return self.__reference
    

    def articles(self):
        """
        Retourne la liste des articles de cette facture.
        """
        return self.__articles
        
    def __str__(self):
        """
        Retourne la reprÃ©sentation string d'une facture, Ã  imprimer avec la mÃ©thode print().
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.articles() :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        Imprime l'entÃªte de la facture, comprenant le descriptif et les tÃªtes de colonnes.
        """
        e = "Facture " + self.description() + "\n"
        e += self.barre_str()
        e += "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC")
        e += self.barre_str()
        return e

    def barre_str(self):
        """
        Retourne un string reprÃ©sentant une barre horizontale sur la largeur de la facture.
        """
        b = ""
        barre_longeur = 83
        for i in range(barre_longeur):
            b += "="
        return b + "\n"

    def article_str(self, art):
        """
        Retourne un string correspondant Ã  une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        Retourne un string reprÃ©sentant une ligne de facture avec les totaux prix et tva, Ã  imprimer en bas de la facture
        """
        b = self.barre_str()
        b += "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix+tva)
        b += self.barre_str()
        return b
        
    # Cette mÃ©thode doit Ãªtre ajoutÃ©e lors de l'Ã©tape 4 de la miasion
    def nombre(self, pce) :
        """
        Retourne le nombre d'exemplaires de la piÃ¨ce pce dans la facture, en totalisant sur tous les articles qui concernent cette piÃ¨ce.
        """
        count=0
        for i in self.articles():
            if i==pce:
                count+=1
        return count

    # Cette mÃ©thode doit Ãªtre ajoutÃ©e lors de l'Ã©tape 5 de la miasion
    def livraison_str(self):
        """
        Cette mÃ©thode est une mÃ©thode auxiliaire pour la mÃ©thode printLivraison
        """
        frag = False
        nbr_tot = 0
        poids_tot = 0
        n_art = 0
        txt = "Livraison - {0}\n{1}\n|{2:<42}|{3:>12}|{4:>12}|{5:>12}|\n{1}".format(self.description(),"="*83,"Description","poids/pce ","nombre ","poids ")
        for a in self.articles():
            if type(a) == ArticlePiece:
                if a.pc.fragile():
                    txt += "| {0:<41}|{1:>9}kg |{2:>11} |{3:>9}kg |\n".format(a.pc.description()+" (!)",a.pc.poids(),a.nombre(),a.pc.poids()*a.nombre())
                else:
                    txt += "| {0:<41}|{1:>9}kg |{2:>11} |{3:>9}kg |\n".format(a.pc.description(),a.pc.poids(),a.nombre(),a.pc.poids()*a.nombre())
                n_art += 1
                nbr_tot += a.nombre()
                poids_tot += a.pc.poids()
                if a.pc.fragile():
                    frag = True
            txt += """{0}\n| {1:<40} |{5:>12}|{2:>11} |{3:>9}kg |
{0}{4}""".format("="*83,"{} articles".format(n_art),nbr_tot,poids_tot,"\n(!) *** livraison fragile ***" if frag else "","")
       
        return txt
