import turtle                # module des graphiques tortue
tortue = turtle.Turtle()     # créer une nouvelle tortue
tortue.speed("fastest")

def square(size, color):
    """Trace un carré plein de taille `size` et de couleur `color`.

    pre: `color` spécifie une couleur.
         La tortue `tortue` est initialisée.
         La tortue est placée à un sommet et orientée en direction d'un
         côté du carré.
    post: Le carré a été tracé sur la droite du premier côté.
          La tortue est à la même position et orientation qu'au départ.
    """
    tortue.color(color)
    tortue.pendown()
    tortue.begin_fill()
    for i in range(4):
        tortue.forward(size)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()

def rectangle_vertical(width, height, color1,color2,color3):
    """
    pre: 'width' est la largeur du rectangle
    'height' la hauteur et 'color' la couleur
    post: dessine un rectangle de taille 'width*height' et
    de couleur 'color'

    """
    tortue.pendown()
    tortue.color(color2)
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(height)
        tortue.right(90)
        tortue.forward(width)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()
    
    tortue.forward(height)
    tortue.pendown()
    tortue.color(color3)
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(height)
        tortue.right(90)
        tortue.forward(width)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()
    
    tortue.backward(height)
    tortue.pendown()
    tortue.color(color1)
    tortue.begin_fill()
    for i in range(2):
        tortue.backward(height)
        tortue.right(90)
        tortue.forward(width)
        tortue.right(90)
    tortue.end_fill()
    tortue.penup()
    
def rectangle_horizontal(width, height, color1,color2,color3):
    """
    pre: 'width' est la largeur du rectangle
    'height' la hauteur et 'color' la couleur
    post: dessine un rectangle de taille 'width*height' et
    de couleur 'color'

    """
    tortue.pendown()
    tortue.color(color3)
    tortue.begin_fill()
    for i in range(2):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
    tortue.end_fill()
    
    tortue.color(color2)
    tortue.begin_fill()
    for i in range(1):
        tortue.left(180)
        tortue.forward(width)
        tortue.left(90)
        tortue.forward(height)
        tortue.left(90)
        tortue.forward(width)
        tortue.left(180)
    tortue.end_fill()
    tortue.penup()
    
    tortue.forward(width)
    tortue.pendown()
    tortue.color(color1)
    tortue.begin_fill()
    for i in range(1):
        tortue.forward(width)
        tortue.right(90)
        tortue.forward(height)
        tortue.right(90)
        tortue.forward(width)
    tortue.end_fill()


def belgian_flag(width):
    """ dessine un drapeau belge de largeur width
    et de proportions 3/2
    
    pre: 'width' est la largeur du rectangle
    'height' la hauteur et 'color' la couleur
    
    post: dessine un rectangle de taille 'width*height' et
    de couleur 'color'

    """
    return rectangle(width,200,"black","yellow","red")


def three_color_flag_Bel(width, color1, color2, color3):
    """ Trace le drapeau de la Belgique
        pre: 'width'>0
        post: trace le drapeau de la Belgique avec
        'width' comme largeur et 'color' comme couleur
    """
    return rectangle_vertical(width,70, "black", "yellow", "red")
three_color_flag_Bel(135, "black", "yellow", "red")

def three_color_flag_Fr(width, color1, color2, color3):
    """ Trace le drapeau de la France
        pre: 'width'>0
        post: trace le drapeau de la France avec
        'width' comme largeur et 'color' comme couleur
    """
    tortue.goto(-400,0)
    return rectangle_vertical(width,70, "blue", "white", "red")
three_color_flag_Fr(135, "blue", "white", "red")



def european_flag(width):
    """ Trace le drapeau de l'UE
        pre: 'width'>0
        post: trace le drapeau de l'UE avec
        'width' comme largeur et 'color' comme couleur
    """
    tortue.goto(-120,300)
    return rectangle_vertical(width,90,"blue","blue","blue")

european_flag(190)

def stars(color,width):
    """ Trace le drapeau de la belgique
        pre: -
        post: dessine les etoiles sur le drapeau de l'UE
        avec 'color' comme couleur
    """
    tortue.color(color)
    tortue.up()
    tortue.goto(1,180)
    tortue.left(90)
    for i in range(12):
        tortue.begin_fill()
        tortue.down()
        for i in range (5):
            tortue.forward(5)
            tortue.right(58)
            tortue.forward(5)
            tortue.left(130)
        tortue.up()
        tortue.forward(45)
        tortue.left(30)
        tortue.end_fill()
stars("yellow",50)


def three_color_flag_Ger(width, color1, color2, color3):
    """ Trace le drapeau de l'Allemagne
        pre: 'width'>0
        post: trace le drapeau de l'Allemagne avec
        'width' comme largeur et 'color' comme couleur
    """
    tortue.goto(600,-40)
    return rectangle_horizontal(width,200, color1, color2, color3)
three_color_flag_Ger(45, "black", "red", "yellow")

def three_color_flag_Lux(width, color1, color2, color3):
    """ Trace le drapeau de l'Allemagne
        pre: 'width'>0
        post: trace le drapeau de l'Allemagne avec
        'width' comme largeur et 'color' comme couleur
    """
    tortue.penup()
    tortue.goto(300,-40)
    return rectangle_horizontal(width,200, color1, color2, color3)
three_color_flag_Lux(45, "AQUA", "white", "red")


def three_color_flag_Holl(width, color1, color2, color3):
    """ Trace le drapeau de l'Allemagne
        pre: 'width'>0
        post: trace le drapeau de l'Allemagne avec
        'width' comme largeur et 'color' comme couleur
    """
    tortue.penup()
    tortue.goto(-800,-45)
    return rectangle_horizontal(width,200, color1, color2, color3)
three_color_flag_Holl(45, "blue", "white", "red")


def voiture(width, height,color1, color2, color3):
    """ Trace le drapeau de l'Allemagne
        pre: 'width'>0
        post: trace le drapeau de l'Allemagne avec
        'width' comme largeur et 'color' comme couleur
    """
    #triangle superieur
    tortue.penup()
    tortue.goto(400,400)
    tortue.pendown()
    tortue.color(color1)
    tortue.begin_fill()
    for i in range(1):
        tortue.right(25)
        tortue.forward(width)
        tortue.right(130)
        tortue.forward(width)
        #inferieur
        tortue.right(50)
        tortue.forward(width)
        tortue.right(130)
        tortue.forward(width)
    tortue.end_fill()
    
    #les cotes
    tortue.begin_fill()
    tortue.color(color1)
    for i in range(1):
        tortue.left(65)
        tortue.forward(width)
        tortue.left(90)
        tortue.forward(height)
    tortue.end_fill()
        
     #le bas
    tortue.begin_fill()
    tortue.color(color2)
    for i in range(1):
        tortue.left(90)
        tortue.forward(5*width)
        tortue.left(90)
        tortue.forward(height)
        tortue.left(90)
        tortue.forward(width)
        #triangle sup et inf 
        tortue.right(70)
        tortue.forward(width)
        tortue.left(130)
        tortue.forward(width)
        tortue.left(50)
        tortue.forward(width)
        tortue.left(130)
        tortue.forward(width)
    tortue.end_fill()
    
    tortue.begin_fill()
    tortue.color(color3)
    for i in range(1):
        tortue.left(120)
        tortue.forward(width-20)
        tortue.forward(width+52)
        tortue.right(90)
        tortue.forward(width-2)
        tortue.right(90)
        tortue.forward(width+68)
        tortue.right(90)
        tortue.forward(width+10)
        tortue.right(15)
        tortue.forward(width-20)
        tortue.right(75)
        tortue.circle(20)
        tortue.forward(width+60)
        tortue.circle(20)
    tortue.end_fill()

voiture(55, 70,"red", "yellow", "green")


def three_color_flag_GN(width, color1, color2, color3):
    """ Trace le drapeau de la Guinée
        pre: 'width'>0
        post: trace le drapeau de la Guinée avec
        'width' comme largeur et 'color' comme couleur
    """
    tortue.penup()
    tortue.goto(-645,300)
    tortue.pendown()
    return rectangle_vertical(width,70, "green", "yellow", "red")
three_color_flag_GN(135, "green", "yellow", "red")



def banderole(width,height,color):
    tortue.penup()
    tortue.color("black",color)
    tortue.begin_fill()
    tortue.pendown()
    tortue.forward(width)
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    tortue.forward(30)
    tortue.left(90)
    tortue.forward(width)
    tortue.right(90)
    tortue.forward(height)
    tortue.left(90)
    tortue.forward(30)
    tortue.left(90)
    tortue.forward(height)
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    tortue.forward(30)
    tortue.left(90)
    tortue.forward(width)
    tortue.right(90)
    tortue.forward(width)
    tortue.left(90)
    tortue.forward(30)
    tortue.end_fill()
    tortue.penup()


def finland_flags(width):
    tortue.penup()
    tortue.goto(-100,-700)
    tortue.pendown()
    rectangle_horizontal(width,410,"blue","blue","blue")
    tortue.penup()
    tortue.goto(-250,-400)
    tortue.left(180)
    banderole(80,340,"GOLD")
    
    
finland_flags(150)




