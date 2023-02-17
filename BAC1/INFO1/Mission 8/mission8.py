class Duree :
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s
        self.temp=self.h*3600+self.m*60+self.s

    def to_secondes(self) :
        """
        Retourne le nombre total de secondes de cette instance de Duree (self).
        """
        if self.h//24!=0 or self.m//60!=0 or self.s//60!=0:
            return 
        else:
            return self.temp

    def delta(self,d) :
        """
        Retourne la différence entre cette instance de Duree (self) et la Duree d passée en paramètre,
        en secondes (positif si ce temps-ci est plus grand).
        """
        return Duree.to_secondes(self)-d.temp        #Ou self.temp-d.temp

    def apres(self,d):
        """
        Retourne True si cette instance de Duree (self) est plus grand que la Duree d passée en paramètre;
        retourne False sinon.
        """
        if self.temp>d.temp:
            return True
        return False
    def ajouter(self,d):
        """
        Ajoute une autre Duree d à cette instance de Duree (self).
        Corrige de manière à ce que les minutes et les secondes soient dans l'intervalle [0..60[,
        en reportant au besoin les valeurs hors limites sur les unités supérieures
        (60 secondes = 1 minute, 60 minutes = 1 heure).
        """
        self.temp+=d.temp
        total_sec=self.temp
        minutes=0
        heures=0
        while total_sec>=60:
            total_sec-=60
            minutes+=1
        while minutes>=60:
            minutes-=60
            heures+=1
        
    

    def __str__(self):
        """
        Retourne cette durée sous la forme de texte "heures:minutes:secondes".
        Astuce: la méthode "{:02}:{:02}:{:02}".format(heures, minutes, secondes)
        retourne le String désiré avec les nombres en deux chiffres en ajoutant
        les zéros nécessaires.
        """
        total_sec=self.temp
        minutes=0
        heures=0
        while total_sec>=60:
            total_sec-=60
            minutes+=1
        while minutes>=60:
            minutes-=60
            heures+=1
        return "{:02}:{:02}:{:02}".format(heures,minutes,total_sec)


class Chanson :
    def __init__(self, t, a, d):
        if type(t)!=str or type(a)!=str or type(d)!=Duree:
            return 
        self.t=t
        self.a=a
        self.d=d
    def __str__(self):
        """
        Retourne un String décrivant cette chanson sous le format "TITRE - AUTEUR - DUREE".
        Par exemple: "Let's_Dance - David_Bowie - 00:04:05"
        """
        return "{} - {} - {}".format(self.t,self.a,self.d)

class Album :
    def __init__(self,n):
        self.n=n
        self.album=[]
        self.duree=Duree(0,0,0)
    def add (self,chanson):
        """
        retourne False si lors de l'ajout d'une chanson lalbum a atteint 100 chansons
        ou la durée dépasserait 75 minutes.
        Sinon la chanson est rajoutée et la méthode add retourne True
        """
        if type(chanson)!=Chanson:
            return
        elif len(self.album)+1==99 or (self.duree.to_secondes()+chanson.d.to_secondes()>75*60):
            return False
        else:
            self.album.append(chanson.__str__())
            self.duree.ajouter(chanson.d)
            return True
       
        
    def __str__(self):
        alB= "Album {} ({} chansons , {})".format(self.n,len(self.album),self.duree)
        for i in range(len(self.album)):
            alB+="\n{:02}: {}".format(i+1,self.album[i])
        return alB


if __name__ == "__main__":
    def lecture(filename):
        l,albm,chanson=[],[],[]
        tot_sec,n=0,1
        with open(filename,"r") as file:
            strings=file.readlines()
            for line in strings:
                l.append(line.strip("\n").split(" "))
        for i in range(len(l)):
            tot_sec+=(Duree(0,int(l[i][2]),int(l[i][3])).to_secondes())
            total_sec=tot_sec
            minutes,heures=0,0
            while total_sec>=60:
                total_sec-=60
                minutes+=1
            while minutes>=60:
                minutes-=60
                heures+=1
            chanson.append(Chanson(l[i][0],l[i][1],Duree(0,int(l[i][2]),int(l[i][3]))))
            total_sec="{:02}:{:02}:{:02}".format(heures,minutes,total_sec)
            if len(albm)+1<=99 or tot_sec<75*60:
                alB= "Album {} ({} chansons {} )".format(n,len(chanson),total_sec)
                index=0
                for i in range(index,len(chanson)):
                    alB+="\n{:02}: {}".format(i+1,chanson[i])
                    albm.append(l[i])
                    index+=1
            else:
               albm=[]
               tot_sec=0
               del chanson[:-1]
               n+=1
               print(alB)
               print("\n")
               index=0
       
       
    print(lecture("music-db.txt"))
   
   


     
   
   