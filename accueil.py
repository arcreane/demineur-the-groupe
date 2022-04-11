import jeu
from tkinter import *

# Création de la fenêtre Window
window = Tk()
window.title("Démineur")
window.configure(bg = "#2515AA")

# Création du Canvas
canva = Canvas(window, width=300, height=300, bg='#2515AA')
canva.pack()

# MENU
# Creation barre menu avec le widget Menu dans le parent window
menuBar = Menu(window)

# Ajout des catégories du menu
# Jouer
menuJouer = Menu(menuBar)
menuBar.add_cascade(label = "Jouer", menu=menuJouer)
# commandes jouer
select = ""
menuJouer.add_radiobutton(label = "Facile", value=1, variable=select, command=lambda: [jeu.initialisation(canva), jeu.creationGrille( 9, 9, 10)])
menuJouer.add_radiobutton(label = "Normal", value=2, variable=select, command=lambda: [jeu.initialisation(canva), jeu.creationGrille(16, 16, 40)])
menuJouer.add_radiobutton(label = "Difficile", value=3, variable=select, command=lambda: [jeu.initialisation(canva), jeu.creationGrille(30, 16, 99)])

# Scores
menuScores = Menu(menuBar)
menuBar.add_command(label = "Scores") 

# Quitter
menuQuitter = Menu(menuBar)
menuBar.add_command(label = "Quitter", command=quit)
window.config(menu=menuBar)



# Afficher
window.mainloop()
