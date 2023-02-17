import math
class Robot:
    def __init__(self,n):
        self.__nom= n      
        self.__x = 0              
        self.__y = 0               
        self.__angle = 0
        self.__history=[]
        
    def __str__(self):
        return f"{self.getnom()}@({round(self.getx())},{round(self.gety())}) angle: {self.getangle()}"
    
    def getnom(self):
        return self.__nom
    
    def gety(self):
        return self.__y
    
    def getanglerad(self) :
        return self.__angle
    
    def position(self):
        return (self.getx(),self.gety())
    
   
    def getHistory(self):
        return self.__history
    
    
    def unplay(self) :
        history = self.getHistory()
        for i in history[::-1] : # parcours la liste dans l'ordre inverse
            if i[0]=="forward":
                self.moveforward(i[1])
                history.remove(i)
                print(("forward",i[1]))
            if i[0]=="backward":
                self.movebackward(i[1])
                history.remove(i)
                print(("backward",(i[1])))
                
            if i[0]=="right":
                self.turnright()
                history.remove(i)
                print(("right",90))
            if i[0]=="left":
                self.turnleft()
                history.remove(i)
                print(("left",90))
                
        # vide l'historique après avoir annulé les actions
        return history
            