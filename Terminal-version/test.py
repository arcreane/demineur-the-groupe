def grille(longueur, largeur):
    """
    Fonction renvoie une grille de taille longueur*largeur
    """
    return [[0 for i in range(largeur)]for i in range(longueur)]

def placer_mines(grille, nb_mines):
    """
    Fonction qui place nb_mines mines dans la grille g
    """
    from random import randint
    count=0
    while count != nb_mines:
        ligne = randint(0,len(grille)-1)
        colonne = randint(0,len(grille[0])-1)
        if grille[ligne][colonne] != -1:
            grille[ligne][colonne] = -1
            count +=1
    return grille

def nombre_voisins(grille, y,x):
    """
    Fonction qui renvoie le nombre de cases vosines contenants une mine
    """
    cpt = 0
    av = 1

    if x<len(grille[y])-1 and grille[y][x+av]==-1:
        cpt+=1
    if y<len(grille)-1 and grille[y+av][x]==-1:
        cpt+=1
    if x>0 and grille[y][x-av]==-1:
        cpt+=1
    if y>0 and grille[y-av][x]==-1:
        cpt+=1

    if x>0 and y>0 and grille[y-av][x-av]==-1:
        cpt+=1
    if y>0 and x<len(grille[y])-1 and grille[y-av][x+av]==-1:
        cpt+=1
    if y<len(grille)-1 and x<len(grille[y])-1 and grille[y+av][x+av]==-1:
        cpt+=1
    if y<len(grille)-1 and x>0 and grille[y+av][x-av]==-1:
        cpt+=1

    return cpt

def definir_nb_voisins(grille):
    """
    Fonction qui renvoie une grille avec pour chaque case le nombre de mines voisines
    """
    grille_voisins = [[0 for i in range(len(grille[0]))]for i in range(len(grille))]
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] != -1:
                grille_voisins[i][j] = nombre_voisins(grille,i,j)
            else:
                grille_voisins[i][j] = -1
    return grille_voisins

def grille_aleatoire(longueur,largeur,nb_mines):
    """
    Fonction qui renvoie un tableau avec les mines qui ont la valeur -1 et les autres, le nombre de mines dans les       cases voisines.
    """
    if nb_mines >= 0 and nb_mines<=longueur*largeur-1:
        g = grille(longueur, largeur)
        g = placer_mines(g, nb_mines)
        return definir_nb_voisins(g)

def afficher_grille_complete(grille):
    """
    fonction qui affiche la grille à la fin
    """
    p="   "
    for i in range(len(grille[0])):
        if i>9:
            p+=" "+str(i)
        else:
            p+="  "+str(i)
    print(p)
    print("")
    for i in range(len(grille)):
        if i<10:
            s=" "
        else:
            s=""
        for j in range(len(grille[0])):

            if grille[i][j]==-1:
                s += "  *"
            elif grille[i][j]!=-1 and nombre_voisins(grille,i,j)==0:
                s += "  ."
            else:
                s+="  "+str(nombre_voisins(grille,i,j))

        print(i, s)

def afficher_grille(grille, revelee):
    """
    Fonction qui affiche la grille de la même façon que
    pour la fonction afficher_grille_complete lorsqu'une case a la valeur True dans le tableau revelee et le                     caractère
'?' lorsqu'elle a la valeur False.
    """
    p="   "
    for i in range(len(grille[0])):
        if i>9:
            p+=" "+str(i)
        else:
            p+="  "+str(i)
    print(p)
    print("")
    for i in range(len(grille)):
        if i<10:
            s=" "
        else:
            s=""
        for j in range(len(grille[0])):

            if revelee[i][j]==False:
                s += "  ?"
            elif revelee[i][j]==True and nombre_voisins(grille,i,j)==0:
                s += "  ."
            else:
                s+="  "+str(nombre_voisins(grille,i,j))

        print(i, s)

def jouer(grille, revelee, x, y):
    """
    Fonction permettant de jouer dans la case de la ligne x et de la colonne y
    grille: tableau d'entiers à deux dimensions
    revelee: tableau de booleen à deux dimensions
    x, y: nombres entiers
    renvoie le tableau revelee après avoir effectuer le coup
    """
    if revelee[x][y]== False:
        revelee[x][y]= True

        if grille[x][y] == 0:
            if(x>0): revelee = jouer(grille, revelee, x-1, y)
            if(x>0 and y>0): revelee = jouer(grille, revelee, x-1, y-1)
            if(y>0): revelee = jouer(grille, revelee, x, y-1)
            if(y>0 and x<len(grille)-1): revelee = jouer(grille, revelee, x+1, y-1)
            if(x<len(grille)-1): revelee = jouer(grille, revelee, x+1, y)
            if(x<len(grille)-1 and y<len(grille[0])-1): revelee = jouer(grille, revelee,
            x+1, y+1)
            if(y<len(grille[0])-1): revelee = jouer(grille, revelee, x, y+1)
            if(x>0 and y<len(grille[0])-1): revelee = jouer(grille, revelee, x-1, y+1)
    return revelee


def victoire(grille, revelee):
    """
    Fonction qui renvoie True si dans le tableau revelee, les cases restantes ayant la valeur False et que dans la grille, l'indice de ces cases ont la valeur -1
    """

    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]!=-1 and revelee[i][j]==False:
                return False
    return True

def defaite(grille,revelee):
    """
    Fonction qui renvoie True si une case contenant une mine est
révélée et False sinon
    """
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]==-1 and revelee[i][j]==True:
                return True
    return False

def jeu(longueur, largeur, nb_mines):
    """
    Jeu du démineur
    """
    grille = grille_aleatoire(longueur, largeur, nb_mines)
    revelee = [[False for i in range(largeur)]for i in range(longueur)]

    while True:

        print("==============================================================================")
        afficher_grille(grille, revelee)
        print("==============================================================================")
        x = int(input("Entrez une abscisse  : "))
        y = int(input("Entrez une ordonnée  : "))
        revelee = jouer(grille, revelee, y, x)

        if defaite(grille, revelee):
            print("==============================================================================")
            print("Vous avez perdu malheureusement ! :(")
            print("==============================================================================")
            break
        elif victoire(grille, revelee):
            print("==============================================================================")
            print("Vous avez gagné ! :)")
            print("==============================================================================")
            break


    afficher_grille_complete(grille)
    print("==============================================================================")

def menu():
    """
    Accueil du joueur dans le jeu, en l'invitant à choisir un niveau de difficulté (débutant,
    intermédiaire ou expert) ou une partie personalisée
    """
    reponse = input("Entrez un niveau de difficulté (Débutant / Intermédiaire / Expert / Partie perso) :")

    if reponse=="Débutant":
        jeu(8,8,10)
    elif reponse=="Intermédiaire":
        jeu(16,16,40)
    elif reponse=="Expert":
        jeu(16,32,99)
    elif reponse=="Partie perso":
        longueur = int(input("Entrez la longueur que vous voulez :"))
        largeur = int(input("Entrez la largeur que vous voulez :"))
        nb_mines = int(input("Entrez le nombre de mines que vous voulez :"))
        jeu(longueur, largeur, nb_mines)
menu()