import random

# Création de la grille grille
grille = []
grilleFinal = []
devoiler = []

colonne = 0
ligne = 0
perdu = False

# Symbole
carre = "◻️ "
vide = "  "
bombe = "💣️"
# carre = "?"
# vide = " "
# bombe = "X"

def creationGrille(niveauColonne, niveauLigne, nbMines):
    global ligne, colonne
    # Ajout colonne et ligne + index
    ligne = niveauLigne + 1
    colonne = niveauColonne + 1
    # Boucle 10 colonne
    for i in range(colonne):
        grille.append([])
        devoiler.append([])
        grilleFinal.append([])
        # Boucle 10 ligne
        for j in range(ligne):
            # Pour chaque lignes, la première case correspond au numero de ligne
            if(j == 0):
                if(i > 0):
                    if(len(str(i)) == 2):
                        grille[i].append(str(i))
                    else:
                        grille[i].append(" " + str(i)) 
                else:
                    grille[i].append(vide)
            # Pour chaque colonnes, la première case correspond au numero de colonne
            if(i == 0):
                if(len(str(j+1)) == 2):
                    grille[i].append(str(j+1))
                else:
                    grille[i].append(" " + str(j+1)) 
            else:
                grille[i].append(carre)
                devoiler[i].append(False)
                grilleFinal[i].append(vide)
    coordsMines()


    # Print de la grille
    for i in range(colonne):
        for j in range(ligne):
            print(grille[i][j], end=" ")
        print()


# def placer_mines(grille, niveauColonne, niveauLigne, nb_mines):
#     totalMine=0
#     while totalMine != nb_mines:
#         ligne = random.randint(0, niveauLigne - 1)
#         colonne = random.randint(0, niveauColonne - 1)

#         grilleFinal[ligne][colonne].append("X")
#     return grilleFinal

# Placement des Mines
def coordsMines():
    for i in range(10):
        nb1 = random.randint(1, 9)
        nb2 = random.randint(1, 9)

        while (grilleFinal[nb1][nb2] != vide):
            nb1 = random.randint(1, 9)
            nb2 = random.randint(1, 9)
        grilleFinal[nb1][nb2] = "💣️"

def joueur():
    x = int(input("Choisissez une ligne : "))
    y = int(input("Choisissez une colonne : "))
    return devoilerCase(x, y)


def devoilerCase(x, y):
    print()
    if(grilleFinal[x][y] == "💣️"):
        grille[x][y] = "💣️"
        print("perdu")
    else:
        grille[x][y] = " ."
        print("vide")

    # Print de la grille
    for i in range(colonne):
        for j in range(ligne):
            # statue[i][j] = True
            print(grille[i][j], end=" ")
        print()
    
    # if():
    #     perdu = True
    # else:
    #     perdu = False



# Logique du Jeu
def logiqueJeu(nbColonne, nbLigne, nbMines ):
    creationGrille(nbColonne, nbLigne, nbMines)
    print("")
    
    while perdu == False:
        joueur()
        
    # Systeme du jeu