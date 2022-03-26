# Création de la grille grille
grille = []

# Taille de la grille
nb_column = 9
nb_ligne = 9

# Symbole
carre = "■"
vide = " "
bombe = "💣️"

row = nb_ligne + 1
column = nb_column + 1

for i in range(column):
    grille.append([])
    for j in range(row):
        if(j == 0):
            if(i < nb_column):
                grille[i].append(i)
            else:
                grille[i].append(vide)
        if(i == nb_column):
            grille[i].append(j)
        else:
            grille[i].append(carre)

for i in range(column):
    for j in range(row):
        print(grille[i][j], end=" ")
    print()
