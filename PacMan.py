#PACMAN LEZGO
import subprocess as subpcs
from colorama import Fore, Back
import pygame

plateau = [[1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,1,1,1,0,1,1,1,0,1],
           [1,0,1,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,1,0,1,1,0,0,0,1],
           [1,1,1,1,0,0,2,0,1,1,0,1],
           [5,0,0,0,0,1,1,0,0,1,0,5],
           [1,1,0,1,1,0,0,1,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,1,1],
           [1,0,1,0,0,0,1,1,0,0,1,1],
           [1,0,0,0,1,0,0,0,0,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1]]
          



pacmanXY = (5,4)


pygame.init()
#Cases Vides === 0
#Murs @ === 1
#PacMan o === 2
#Points * === 3
#Fantomes # === 4
#Teleporteurs === 5

def longeur(liste):
    return (len(liste[0])-1)

def hauteur(liste):
    return (len(liste)-1)


#Check if PacMan can move in a certain direction
#ml = main list (liste principale qui contient elle même des listes)
#eil = element in list (elements dans la liste)


def ismovable(liste, ml, eil):
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
    elif uinp == "d":
        res = "right"
    return res



#Detecting if a key is pressed (ZQSD) 

def moving(liste, uinp):
    if uinp == "up" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[0]:
        pacmanXY[0]+=1
    elif uinp == "down" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[1]:
        pacmanXY[0]-=1
    elif uinp == "right" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[2]:
        pacmanXY[1]+=1
    elif uinp == "left" and (ismovable(liste, (pacmanXY[0], pacmanXY[1])))[3]:
        pacmanXY[1]-=1






#Dessin du playground
def dessinplateau(liste):
    for j in range(len(liste)):
        #print(Back.BLACK, Fore.WHITE)
        for k in range(len(liste[0])):
            #print(Back.BLACK, Fore.WHITE, end = "")
            if liste[j][k] == 1:
                print("@",  end = "")
            elif liste[j][k] == 2:
                print("o", end = "")
            elif liste[j][k] == 3:
                print("*", end = "")
            elif liste[j][k] == 4:
                print("#", end = "")
            elif (liste[j][k] == 0) or (liste[j][k] == 5):
                print(" ", end = "")
        print()

'''
def on_press(uinp):
    if uinp == "z":
        res = "up"
    elif uinp == "q":
        res = "left"
    elif uinp == "s":
        res = "down"
    elif uinp == "d":
        res = "right"
    else:
        res = ""
    return res
'''

#Fonction pour mettre les bonnes valeurs de pour les cases adjacentes 
def adjacent(liste, uinp):
    x = pacmanXY[0]
    y = pacmanXY[1]
    futureV = (x, y)
    if uinp == "up":
        futureV = (x+1, y)
    elif uinp == "down":
        futureV = (x-1, y)
    elif uinp == "left":
        futureV = (x, y-1)
    elif uinp == "right":
        futureV = (x, y+1)
    return futureV



#Fonction pour detecter la mort
def alive(liste, uinp):
    vie = True
    if liste[adjacent(liste, uinp)[0]][adjacent(liste, uinp)[1]] == 4:
        vie = False
    elif liste[adjacent(liste, uinp)[0]][adjacent(liste, uinp)[1]] == 4:
        vie = False
    elif liste[adjacent(liste, uinp)[0]][adjacent(liste, uinp)[1]] == 4:
        vie = False
    elif liste[adjacent(liste, uinp)[0]][adjacent(liste, uinp)[1]] == 4:
        vie = False
    return vie




#Fonction pour savoir si le joueur a gagné la partie
#cp === Current Points, mp === Maximum achievable Points
def end (cp, mp):
    result = False
    if cp == mp:
        result = True
    return result

#Main Fonction

def PacMan(liste):
    envie = True
    fin = False
    uinp = ""
    while envie or (not fin):
        subpcs.run("clear")
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.type == pygame.K_UP:
                    uinp = "up"
                elif i.type == pygame.K_DOWN:
                    uinp = "down"
                elif i.type == pygame.K_LEFT:
                    uinp = "left"
                elif i.type == pygame.K_RIGHT:
                    uinp = "right"
                else:
                    pass
            else:
                pass

        envie = alive(liste, uinp)
        #fin = end(cp, mp)
        dessinplateau(liste)
        moving(liste, uinp)


PacMan(plateau)




        





