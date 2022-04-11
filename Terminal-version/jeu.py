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
                    grille[i].append(str(i).zfill(2))
                else:
                    grille[i].append(vide)
            # Pour chaque colonnes, la première case correspond au numero de colonne
            if(i == 0):
                grille[i].append(str(j+1).zfill(2))
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
    nb1Tableau = []
    nb2Tableau = []
    for i in range(10):
        nb1 = random.randint(1, 9)
        nb2 = random.randint(1, 9)
        nb1Tableau.append(nb1)
        nb2Tableau.append(nb2)
        grilleFinal[nb1Tableau[i]][nb2Tableau[i]] = "💣️"
    # print(grille.count("💣️"))

# def nombre_voisins(grille, y,x):
#     """
#     Fonction qui renvoie le nombre de cases vosines contenants une mine
#     """
#     cpt = 0
#     av = 1

#     if x<len(grille[y])-1 and grille[y][x+av]==-1:
#         cpt+=1
#     if y<len(grille)-1 and grille[y+av][x]==-1:
#         cpt+=1
#     if x>0 and grille[y][x-av]==-1:
#         cpt+=1
#     if y>0 and grille[y-av][x]==-1:
#         cpt+=1

#     if x>0 and y>0 and grille[y-av][x-av]==-1:
#         cpt+=1
#     if y>0 and x<len(grille[y])-1 and grille[y-av][x+av]==-1:
#         cpt+=1
#     if y<len(grille)-1 and x<len(grille[y])-1 and grille[y+av][x+av]==-1:
#         cpt+=1
#     if y<len(grille)-1 and x>0 and grille[y+av][x-av]==-1:
#         cpt+=1

#     return cpt



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
        grille[x][y] = "."
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