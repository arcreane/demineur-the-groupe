from tkinter import *
import random

grille = []
b = []
presenceBombe = []
canva = ""
colonne = 0
ligne = 0
mines = 0
numCase = 0
maxCase = 0


# Vider la grille
def initialisation(canvas):
    global grille, b, canva
    canva = canvas
    for i in grille:
        i.destroy()
    for j in b:
        j.destroy()
    canva.delete("all")

# Creation de la grille
def creationGrille(niveauColonne, niveauLigne, niveauMines):
    global maxCase, numCase, colonne, ligne, mines
    colonne = niveauColonne
    ligne = niveauLigne
    mines = niveauMines
    maxCase = colonne * ligne - 1

    for i in range(niveauColonne):
        for j in range(niveauLigne):
            grille.append(Label(canva, text=" ", bd=1, width=1, height=1,padx=9,pady=5, relief=SUNKEN))
            grille[numCase].grid(row=j, column=i)
    
            # for i in range(mines):
            #     nb1 = random.randint(0, maxCase)
            #     while nb1 in presenceBombe:
            #             nb1 = random.randint(0, maxCase)
            #     presenceBombe.append(nb1)
            #     grille[nb1].config(text="B", relief = GROOVE, bd=1,width=0,height=0)
            #     presenceBombe.append(numCase)

            # b.append(Button(canva,text="",image="",padx=8,pady=1)) 
            # b[numCase].grid(row=j, column=i)
            # b[numCase].bind("<Button-1>", lambda i, coord=numCase: click(coord))
            # b[numCase].config(relief=RAISED)
            
            numCase +=1
    # coordsMines()
    

# def coordsMines():
#     global grille, maxCase,  mines, numCase
#     presenceBombe = []
    
#     for i in range(mines):
#         nb1 = random.randint(0, maxCase)
#         while nb1 in presenceBombe:
#                 nb1 = random.randint(0, maxCase)
#         presenceBombe.append(nb1)
#         grille[nb1].config(text="B", relief = GROOVE, bd=1,width=0,height=0)
#         presenceBombe.append(numCase)

    








# photo= PhotoImage(file="img/bombe.png")

# mines
# def click(coord):
#     b[coord].grid_forget()
#     # verifGagne(grille, coord)
    

# def coordsMines():
#     global presenceBombe
    
#     for i in range(mines):
#         nb1 = random.randint(0, maxCase)
#         while nb1 in presenceBombe:
#                 nb1 = random.randint(0, maxCase)
#         presenceBombe.append(nb1)
#         grille[nb1].config(text="B", relief = GROOVE, bd=1,width=0,height=0)
#         presenceBombe.append(numCase)

    # for i in presenceBombe:
    #     nbVoisines = 0
    #     for i in range(ligne-1, ligne+2):
    #         for j in range(colonne-1, colonne+2):
    #             nbVoisines += grille[i][j]
    #             grille[j].config(text="1")
 

# def verifGagne(grille, coord):
#     if grille[coord].cget("text") == "B":
#         perdu()

# def perdu():
    
#     perdu = Tk()
#     perdu.title("Démineur")
#     perdu.config(bg="#2515AA")
#     messagePerdu = Text(perdu, text = "BOUM! Vous avez perdu.", fg="Arial, 10")
#     messagePerdu.pack(expand=CENTER)
#     perdu.mainloop()


# # def supprimer(b, coord):
# #     maxCase = len(coord)
# #     for i in maxCase:
# #         b[i].grid_forget()





# if not(i == 0 and j == 0):
#     nbVoisines += grille[ligne + 1][colonne + j]
# grille[ligne + 1][colonne + j].set("C")
            
