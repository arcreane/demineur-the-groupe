
# Création de la grille grille
grille = []

# Symbole
carre = "◻️ "
vide = "  "
bombe = "💣️"

def creationGrille(niveauColonne, niveauLigne):
    # Ajout colonne et ligne + index
    ligne = niveauLigne + 1
    colonne = niveauColonne + 1
    # Boucle 10 colonne
    for i in range(colonne):
        grille.append([])
        # Boucle 10 ligne
        for j in range(ligne):
            # Pour chaque lignes, la première case correspond au numero de ligne
            if(j == 0):
                if(i > 0):
                    grille[i].append(str(i).zfill(2))
                else:
                    grille[i].append(vide)
            # Pour chaque colonnes, la dernière case correspond au numero de colonne
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
        if(grille[nb1Tableau[i]][nb2Tableau[i]] == carre):
            grille[nb1Tableau[i]][nb2Tableau[i]] = "💣️"
    print(grille.count("💣️"))

# Logique du Jeu
def logiqueJeu(niveauColonne, niveauLigne):
    creationGrille(niveauColonne, niveauLigne)
    print("")
    coordsMines()
    # Systeme du jeu
