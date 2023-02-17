#Importation des bibliothéques necessaires
import pygame
from pygame.locals import*

#Initialisation de la bibliothèque Pygame
pygame.init()

#Creation de la fenetre
fenetre=pygame.display.set_mode((640,480),RESIZABLE)

#Charger une image
fond=pygame.image.load("background.jpg").convert()

fenetre.blit(fond,(0,0))

#Mettre à jour l'image pygame entière
pygame.display.flip()

#Variable qui continue la boucle si =1 , stoppe si=0
continuer=1

#Une boucle infinie qui garde la fenetre ouverte
while continuer:
    continuer=int(input())


