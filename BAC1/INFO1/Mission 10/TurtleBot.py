import turtle
from Robot import*
import math

class TurtleBot(Robot):
    def __init__(self,nom):
        super().__init__(nom)
        self.__nom=nom
        self.__x=0
        self.__y=0
        self.__angle=0
        self.t=turtle.Turtle()
        self.__history=[]
        
    def __str__(self):
        return super().__str__()

    def getnom(self):
        return super().getnom()
    def getx(self):
        return self.__x
    def gety(self):
        return super().gety()
    def getanglerad(self) :
        return super().getanglerad()
    def getangle(self):
        return ( self.__angle * 180 / math.pi ) % 360
    
        
    def setx(self,x) :
        self.__x = x
        
    def sety(self,y) :
        self.__y = y
    
    def position(self):
        return super().position()
    
        
    def move(self,distance,sense) :
        """ mÃ©thode auxiliaire pour faire avancer ou reculer le robot en dessinant sa trace
            si sense = 1  il avance de distance pixels
            si sense = -1 il recule de distance pixels
        """
        oldx = self.getx()
        oldy = self.gety()
        orientationx = math.cos(self.getanglerad())
        orientationy = math.sin(self.getanglerad())
        self.setx(oldx + orientationx * distance * sense)
        self.sety(oldy + orientationy * distance * sense)

    def moveforward(self,distance) :
        """ fait avancer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.move(distance,1)
        self.t.forward(distance)
        super().getHistory().append(("forward",distance))

    def movebackward(self,distance) :
        """ fait reculer le robot de distances pixels et trace une ligne lors de ce mouvement """
        self.move(distance,-1)
        self.t.backward(distance)
        super().getHistory().append(("backward",distance))

    def __turn(self,direction) :
        """ mÃ©thode auxiliaire pour les mÃ©thodes turnright() et turnleft()
            si direction = 1 elle change l'angle du robot de 90 degrÃ©s vers la droite (dans le sens des aiguilles d'une montre)
            si direction = -1 elle change l'angle du robot de 90 degrÃ©s vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__angle = self.__angle + direction * math.pi/2
        
    def turnright(self) :
        """ fait tourner le robot de 90 degrÃ©s vers la droite (dans le sens des aiguilles d'une montre)
        """
        self.__turn(-1)
        self.t.right(90)
        super().getHistory().append(("right",90))
        
    def turnleft(self) :
        """ fait tourner le robot de 90 degrÃ©s vers la gauche (dans le sens contraire des aiguilles d'une montre)
        """
        self.__turn(1)
        self.t.left(90)
        super().getHistory().append(("left",90))
        
    def getHistory(self):
        return super().getHistory()
    
    
    def unplay(self) :
        return super().unplay() 
    
if __name__ == '__main__':   
    r2d2 = TurtleBot("R2-D2")

    # first move to position (100,100) facing East, to be more or less in the center of the window
    r2d2.moveforward(100)
    r2d2.turnright()
    r2d2.moveforward(100)
    r2d2.turnleft()

    print(r2d2)
    #R2-D2@(100, 100) angle: 0.0
    r2d2.moveforward(50)
    r2d2.turnleft()
    print(r2d2)
    #R2-D2@(150, 100) angle: 270.0
    r2d2.moveforward(50)
    r2d2.turnleft()
    print(r2d2)
    #R2-D2@(150.0, 50.0) angle: 180.0
    r2d2.moveforward(50)
    r2d2.turnleft()
    print(r2d2)
    #R2-D2@(100.0, 50.0) angle: 90.0
    r2d2.moveforward(50)
    print(r2d2)
    #R2-D2@(100, 100) angle: 90.0
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)
    r2d2.moveforward(50)
    r2d2.turnright()
    print(r2d2)

    
    print(r2d2.getHistory())
    print(r2d2.unplay())



