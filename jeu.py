
# Création de la grille grille
grille = []

# Symbole
carre = "■ "
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
                if(i < niveauColonne):
                    grille[i].append(str(i).zfill(2))
                else:
                    grille[i].append(vide)
            # Pour chaque colonnes, la dernière case correspond au numero de colonne
            if(i == niveauColonne):
                grille[i].append(str(j).zfill(2))
            else:
                grille[i].append(carre)
    # Print de la grille
    for i in range(colonne):
        for j in range(ligne):
            print(grille[i][j], end=" ")
        print()

# Logique du Jeu
def logiqueJeu(niveauColonne, niveauLigne):
    creationGrille(niveauColonne, niveauLigne)
    print("")
    # Systeme du jeu
