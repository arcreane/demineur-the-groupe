import random
from tkinter import *

grille = []
b = []

# grille
def creationGrille(window, niveauColonne, niveauLigne, mines):
    
    canva = Canvas(window, width=300, height=300, bg='#2515AA')
    numCase = 0
    maxCase = niveauColonne * niveauLigne -1
    for i in range(niveauColonne):
        for j in range(niveauLigne):
            grille.append(Label(canva, text=v, bd=1, width=1, height=1,padx=9,pady=5, relief=SUNKEN))
            grille[numCase].grid(row=j, column=i)

            # b.append(Button(canva,text="",image="",padx=8,pady=1)) 
            # b[numCase].grid(row=j, column=i)
            # b[numCase].bind("<Button-1>", lambda i, coord=numCase: click(grille, b, coord))
            # b[numCase].config(relief=RAISED)
            numCase +=1
    # compteMinesVoisines(grille, niveauLigne, niveauColonne)
    coordsMines(grille, maxCase, numCase, mines)
    canva.pack()
    
#  Chiffres
# def compteMinesVoisines(grille, ligne, colonne):
#     nbVoisines = 0
#     for i in range(ligne-1, ligne+2):
#         for j in range(colonne-1, colonne+2):
#             if i >= 0 and i < len(grille) and j >= 0 and j < len(grille[ligne]):
#                 nbVoisines += grille[i][j]
#     return nbVoisines
                
# photo= PhotoImage(file="img/bombe.png")

# mines

def click(grille, b, coord):
    b[coord].grid_forget()
    verifGagne(grille, coord)

def coordsMines(grille, maxCase, numCase, mines):
    for i in range(mines):
        nb1 = random.randint(0, 8)
        nb2 = random.randint(0, 8)

        grille[nb1][nb2].config(text=0, relief = GROOVE, bd=1,width=0,height=0)

        # while nb1 in presenceBombe:
        #         nb1 = random.randint (0, maxCase)
        # presenceBombe.append(nb1)
        # grille[nb1].config(text="B", relief = GROOVE, bd=1,width=0,height=0)
        # presenceBombe.append(numCase)

def verifGagne(grille, coord):
    if grille[coord].cget("text") == "B":
        perdu()

def perdu():
    
    perdu = Tk()
    perdu.title("Démineur")
    perdu.config(bg="#2515AA")
    messagePerdu = Text(perdu, text = "BOUM! Vous avez perdu.", fg="Arial, 10")
    messagePerdu.pack(expand=CENTER)
    perdu.mainloop()


# def supprimer(b, coord):
#     maxCase = len(coord)
#     for i in maxCase:
#         b[i].grid_forget()

###### Variables ######

v= " "