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
          



pacmanXY = (5,4)



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


def ismovable(liste, (ml, eil)):
    if liste[ml+1][eil] != 1:
        up = True
    if liste[ml-1][eil] != 1:
        down = True
    if liste[ml][eil+1] != 1:
        right = True
    if liste[ml][eil-1] != 1:
        left = True
    return (up, down, right, left)

#Converting keys to values
def quellecase(uinp):
    if uinp == "z":
        res = "up"
    elif uinp == "q":
        res = "left"
    elif uinp == "s":
        res = "down"
    elif uinp = "d":
        res = "right"
    return res



#Detecting if a key is pressed (ZQSD) 

def moving(liste, (ml, eil), uinp):
    if uinp == "up" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[0]:
        pacmanXY[0]+=1
    elif uinp == "down" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[1]:
        pacmanXY[0]-=1
    elif uinp == "right" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[2]:
        pacmanXY[1]+=1
    elif uinp == "left" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[3]:
        pacmanXY[1]-=1





