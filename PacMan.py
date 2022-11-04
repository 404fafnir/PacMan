#PACMAN LEZGO
import subprocess as subpcs
from colorama import Fore, Back

plateau = [[1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,1,1,1,0,1,1,1,0,1],
           [1,0,1,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,1,0,1,1,0,0,0,1],
           [1,1,1,1,0,0,0,0,1,1,0,1],
           [0,0,0,0,0,1,1,0,0,1,0,0],
           [1,1,0,1,1,0,0,1,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,1,1],
           [1,0,1,0,0,0,1,1,0,0,1,1],
           [1,0,0,0,1,0,0,0,0,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1]]
          



#PacMan o 
#Points *
#Fantomes #

def longeur(liste):
    return (len(liste[0])-1)

def hauteur(liste):
    return (len(liste)-1)


#Check if PacMan can move in a certain direction
#ml = main list (liste principale qui contient elle même des listes)
#eil = element in list (elements dans la liste)


def movable(liste, (ml,eil)):
    if liste[ml+1][eil] == 1:
        up = False
    if liste[ml-1][eil] == 1:
        down = False
    if liste[ml][eil+1] == 1:
        right = False
    if liste[ml][eil-1] == 1:
        left = False
    return (up, down, right, left)





