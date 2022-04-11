import random

# Création de la grille grille
grille = []
statue = []

colonne = 0
ligne = 0

# Symbole
carre = "◻️ "
vide = "  "
bombe = "💣️"
# carre = "?"
# vide = " "
# bombe = "X"

def creationGrille(niveauColonne, niveauLigne):
    global ligne, colonne
    # Ajout colonne et ligne + index
    ligne = niveauLigne + 1
    colonne = niveauColonne + 1
    # Boucle 10 colonne
    for i in range(colonne):
        grille.append([])
        statue.append([])
        # Boucle 10 ligne
        for j in range(ligne):
            # Pour chaque lignes, la première case correspond au numero de ligne
            if(j == 0):
                if(i > 0):
                    grille[i].append(str(i).zfill(2))
                else:
                    grille[i].append(vide)
            # Pour chaque colonnes, la première case correspond au numero de colonne
            if(i == 0):
                grille[i].append(str(j+1).zfill(2))
            else:
                grille[i].append(carre)
    # Print de la grille
    for i in range(colonne):
        for j in range(ligne):
            print(grille[i][j], end=" ")
        print()


# Placement des Mines
def coordsMines():
    nb1Tableau = []
    nb2Tableau = []
    for i in range(10):
        nb1 = random.randint(1, 9)
        nb2 = random.randint(1, 9)
        nb1Tableau.append(nb1)
        nb2Tableau.append(nb2)
        grille[nb1Tableau[i]][nb2Tableau[i]] = "💣️"
    print(grille.count("💣️"))

def joueur():
    x = int(input("Choisissez une ligne : "))
    y = int(input("Choisissez une colonne : "))
    return devoilerCase(x, y)


def devoilerCase(x, y):
    print()
    grille[y][x] = 0

    # Print de la grille
    for i in range(colonne):
        for j in range(ligne):
            # statue[i][j] = True
            print(grille[i][j], end=" ")
        print()



# Logique du Jeu
def logiqueJeu(niveauColonne, niveauLigne):
    creationGrille(niveauColonne, niveauLigne)
    print("")
    joueur()
    # Systeme du jeu