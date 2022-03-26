# Création de la grille grille
grille = []

# Taille de la grille
nb_colonne = 9
nb_ligne = 9

# Symbole
carre = "■"
vide = " "
bombe = "💣️"

# Ajout colonne et ligne + index
ligne = nb_ligne + 1
colonne = nb_colonne + 1

# Boucle 10 colonne
for i in range(colonne):
    grille.append([])
    # Boucle 10 ligne
    for j in range(ligne):
        # Pour chaque lignes, la première case correspond au numero de ligne
        if(j == 0):
            if(i < nb_colonne):
                grille[i].append(i)
            else:
                grille[i].append(vide)
        # Pour chaque colonnes, la dernière case correspond au numero de colonne
        if(i == nb_colonne):
            grille[i].append(j)
        else:
            grille[i].append(carre)

# Print de la grille
for i in range(colonne):
    for j in range(ligne):
        print(grille[i][j], end=" ")
    print()
