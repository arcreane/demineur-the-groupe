# Création de la grille grille
grille = []

# Taille de la grille
niveauColonne = 9
niveauLigne = 9

# Symbole
carre = "■"
vide = " "
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
                    grille[i].append(i)
                else:
                    grille[i].append(vide)
            # Pour chaque colonnes, la dernière case correspond au numero de colonne
            if(i == niveauColonne):
                grille[i].append(j)
            else:
                grille[i].append(carre)
    # Print de la grille
    for i in range(colonne):
        for j in range(ligne):
            print(grille[i][j], end=" ")
        print()

# creationGrille(niveauColonne, niveauLigne)

# AFFICHAGES

# Accueil
def accueil():
    # Titre
    for i in range(5):
        if(i == 0 or i == 4):
            print(bombe + ("*" * 60) + bombe)
        elif(i == 1 or i == 3):
            print("*" + 61* " " + "*")
        elif(i == 2):
            print("*" + " " * 14 + bombe + " Bienvenue sur le démineur "+ bombe + " " * 16 + "*")
    print(" ")
    # Options
    choix1 = "1. Jouer"
    choix2 = "2. Voir mes scores"
    choix3 = "3. Quitter"
    print("Choisissez une option : ")
    print(choix1 + "\n" + choix2 + "\n" + choix3 + "\n")
    joueur = int(input("Quel est votre choix ? "))
    if(joueur == 1):
        niveauChoix()
    elif(joueur == 2):
        scores()
    elif(joueur == 3):
        quitter()
    else:
        print("Veuillez saisir le chiffre correspondant à votre choix")

# Niveaux
def niveauChoix():
    # Proposer niveau ou retour au menu
    print("Choisissez un niveau de difficulté : ")
    niveau1 = "1. Facile"
    niveau2 = "2. Normal"
    niveau3 = "3. Difficile"
    retour = "4. Retourner au Menu"
    print(niveau1 + "\n" + niveau2 + "\n" + niveau3 + "\n" + retour)
    joueur = int(input("Quel est votre choix ? "))
    if(joueur == 1):
        niveauColonne = 9
        niveauLigne = 9
        print("Vous avez choisie le niveau : Facile\n")
    elif(joueur == 2):
        niveauColonne = 16
        niveauLigne = 16
        print("Vous avez choisie le niveau : Normal\n")
    elif(joueur == 3):
        niveauColonne = 16
        niveauLigne = 30
        print("Vous avez choisie le niveau : Difficile\n")
    elif(joueur == 4):
        accueil()
    else:
        print("Veuillez saisir le chiffre correspondant à votre choix\n")
        print(niveau1 + "\n" + niveau2 + "\n" + niveau3 + "\n" + retour)
        joueur = int(input("Quel est votre choix ? "))

# Scores
def scores():
    pass

# Quitter
def quitter():
    pass


def menu():
    # ACCUEIL
    accueil()
menu()