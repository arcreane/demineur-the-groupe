import random
from tkinter import *

# grille
def creationGrille(window, niveauColonne, niveauLigne, mines):
    canva = Canvas(window, width=300, height=300, bg='ivory')
    for i in range(niveauColonne):
        for j in range(niveauLigne):
            button = Button(canva,bd=2,width=2,height=1, background="white")
            button.grid(row=j, column=i)
    # coordsMines(mines, canva)
    canva.pack()


# mines
# def coordsMines(mines, canva):
#     nb1Tableau = []
#     nb2Tableau = []
#     for i in range(mines):
#         nb1 = random.randint(1, 9)
#         nb2 = random.randint(1, 9)
#         nb1Tableau.append(nb1)
#         nb2Tableau.append(nb2)
#         # mines = Button(canva, text="T", width=2,height=1)
#         # mines.grid(row = nb1Tableau[i], column = nb2Tableau[i])

