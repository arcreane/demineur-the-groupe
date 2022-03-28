import random
from tkinter import *
from turtle import width

# grille
grille = []
def creationGrille(window, niveauColonne, niveauLigne, mines):
    canva = Canvas(window, width=300, height=300, bg='ivory')
    numCase = 0
    maxCase = niveauColonne * niveauLigne -1
    for i in range(niveauColonne):
        for j in range(niveauLigne):
            grille.append(Label(canva, text="", bd=1, width=1, height=1,padx=9,pady=5, relief=RAISED))
            # button = Button(canva,bd=2,width=2,height=1, background="white")  #relief ="GROOVE"
            coord = numCase
            grille[numCase].grid(row=j, column=i)
            grille[numCase].bind("<Button-1>", click(coord))
            numCase +=1
    coordsMines(maxCase, numCase, mines, canva)
    canva.pack()

def click(coord):
    pass

bombeImg = PhotoImage(file="img/bombe.png")
# mines
def coordsMines(maxCase, numCase, mines, canva):
    presenceBombe = []
    for i in range(mines):
        nb1 = random.randint(0, maxCase)
        while nb1 in presenceBombe:
                nb1 = random.randint(0, maxCase)
        presenceBombe.append(nb1)
        grille[nb1].config(image=bombeImg, relief = GROOVE, bd=1,width=0,height=0)
        presenceBombe.append(numCase)

