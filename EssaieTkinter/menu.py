import grille
from tkinter import *

def fenetre(window, select,niveauColonne, niveauLigne, mines):
    if select == 1:
        window.destroy()
        facile = Tk()
        facile.title("Démineur")
        facile.config(bg="#2515AA")
        menuSelonFenetre(facile)
        grille.creationGrille(facile,niveauColonne, niveauLigne, mines)

    if select == 2:
        window.destroy()
        normal = Tk()
        normal.title("Démineur")
        normal.config(bg="#2515AA")
        menuSelonFenetre(normal)
        grille.creationGrille(normal,niveauColonne, niveauLigne, mines)
    if select == 3:
        window.destroy()
        difficile = Tk()
        difficile.title("Démineur")
        difficile.config(bg="#2515AA")
        menuSelonFenetre(difficile)
        grille.creationGrille(difficile,niveauColonne, niveauLigne, mines)

def menuSelonFenetre(window):
    # Creation barre menu avec le widget Menu dans le parent window
    menuBar = Menu(window)


    # canva = Canvas(window, width=300, height=300, bg='ivory')
    # Ajout des catégories du menu
    # Jouer
    menuJouer = Menu(menuBar)
    menuBar.add_cascade(label = "Jouer", menu=menuJouer)
    # commandes jouer
    select = ""
    menuJouer.add_radiobutton(label = "Facile", value=1, variable=select, command=lambda: fenetre(window, 1, 9, 9, 10))
    menuJouer.add_radiobutton(label = "Normal", value=2, variable=select, command=lambda: fenetre(window, 2, 16, 16, 40))
    menuJouer.add_radiobutton(label = "Difficile", value=3, variable=select, command=lambda: fenetre(window, 3, 30, 16, 99))

    # Scores
    menuScores = Menu(menuBar)
    menuBar.add_command(label = "Scores") 

    # Quitter
    menuQuitter = Menu(menuBar)
    menuBar.add_command(label = "Quitter", command=quit)
    window.config(menu=menuBar)
