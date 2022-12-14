#PACMAN LEZGO
import subprocess as subpcs
import curses


stdscr = curses.initscr()

plateau = [[1,1,1,1,1,1,1,1,1,1,1,1],
           [1,2,0,0,0,0,0,0,0,0,0,1],
           [1,0,1,1,1,1,0,1,1,1,0,1],
           [1,0,1,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,1,0,1,1,0,0,0,1],
           [1,1,1,1,0,0,0,0,1,1,0,1],
           [5,0,0,0,0,1,1,0,0,1,0,5],
           [1,1,0,1,1,0,0,1,0,0,0,1],
           [1,0,0,1,0,0,0,0,0,0,1,1],
           [1,0,1,0,0,0,1,1,0,0,1,1],
           [1,0,0,0,1,0,0,0,0,1,1,1],
           [1,1,1,1,1,1,1,1,1,1,1,1]]
          


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
#x = main list (liste principale qui contient elle même des listes)
#y = element in list (elements dans la liste)


def ismovable(liste, x, y):
    if liste[x+1][y] == 1:
        up = False
    if liste[x-1][y] == 1:
        down = False
    if liste[x][y+1] == 1:
        right = False
    if liste[x][y-1] == 1:
        left = False
    return (up, down, right, left)

'''
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
'''


#Detecting if a key is pressed and modify the list 

def moving(liste, uinp, x, y):
    if uinp == "up" and (ismovable(liste, x, y))[0]:
        liste[x][y] = 0
        x+=1
        liste[x][y] = 2
    elif uinp == "down" and (ismovable(liste, x, y))[1]:
        liste[x][y] = 0
        x-=1
        liste[x][y] = 2
    elif uinp == "right" and (ismovable(liste, x, y))[2]:
        liste[x][y] = 0
        y+=1
        liste[x][y[1]] = 2
    elif uinp == "left" and (ismovable(liste, x, y))[3]:
        liste[x][y] = 0
        y-=1
        liste[x][y] = 2
    return x, y






#Dessin du playground
def dessinplateau(liste):
    for j in range(len(liste)):
        for k in range(len(liste[0])):
            if liste[j][k] == 1:
                stdscr.addstr("@")
            elif liste[j][k] == 2:
                stdscr.addstr("o")
            elif liste[j][k] == 3:
                stdscr.addstr("*")
            elif liste[j][k] == 4:
                stdscr.addstr("#")
            elif (liste[j][k] == 0) or (liste[j][k] == 5):
                stdscr.addstr(" ")
        stdscr.addstr("\n")



#Fonction pour savoir la valeurs des cases autours 
def adjacent(liste, uinp, x, y):
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
def alive(liste, x, y):
    vie = True
    if liste[x+1][y] == 4:
        vie = False
    elif liste[x-1][y] == 4:
        vie = False
    elif liste[x][y-1] == 4:
        vie = False
    elif liste[x][y+1] == 4:
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
    
    curses.noecho()
    envie = True
    fin = False
    x = 1
    y = 1

    while envie or (not fin):
        
        dessinplateau(liste)
            
        c = stdscr.getch()
    
        if (c == ord('z') or c == curses.KEY_UP):
            moving(liste, "up", x, y)
        elif (c == ord('s') or c == curses.KEY_DOWN):
            moving(liste, "down", x, y)
        elif (c == ord('q') or c == curses.KEY_LEFT):
            moving(liste, "left", x , y)
        elif (c == ord('d') or c == curses.KEY_RIGHT):
            moving(liste, "right", x, y)
        stdscr.refresh()
        envie = alive(liste, x, y)
        #fin = end(cp, mp)
        
    curses.endwin()


PacMan(plateau)




        





