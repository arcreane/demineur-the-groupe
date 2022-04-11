import jeu
import score
# MENU

# Accueil
def accueil():
    # Titre
    for i in range(5):
        if(i in [0, 4]):
            print("💣️" + ("*" * 60) + "💣️")
        elif(i in [1, 3]):
            print("*" + 61* " " + "*")
        elif(i == 2):
            print("*" + " " * 14 + "💣️" + " Bienvenue sur le démineur "+ "💣️" + " " * 16 + "*")
    print(" ")
    # Options
    choix1 = "1. Jouer"
    choix2 = "2. Voir mes scores"
    choix3 = "3. Quitter"
    print("Choisissez une option : ")
    print(choix1 + "\n" + choix2 + "\n" + choix3 + "\n")
    joueur = input("Quel est votre choix ? ")
    print(" ")
    while(True):
        try: 
            if(int(joueur) not in [1, 2, 3]):
                print("Veuillez saisir le chiffre correspondant à votre choix")
                joueur = input("Quel est votre choix ? ")
            else:
                break
        except ValueError:
            print("Veuillez saisir le chiffre correspondant à votre choix")
            joueur = input("Quel est votre choix ? ")
        print(" ")
    if(int(joueur) == 1):
        niveauChoix()
    elif(int(joueur) == 2):
        score.scores()
    elif(int(joueur) == 3):
        quitter()
        

# Niveaux
def niveauChoix():
    # Proposer niveau ou retour au menu
    print("Choisissez un niveau de difficulté : ")
    niveau1 = "1. Facile"
    niveau2 = "2. Normal"
    niveau3 = "3. Difficile"
    retour = "4. Retourner au Menu"
    print(niveau1 + "\n" + niveau2 + "\n" + niveau3 + "\n" + retour + "\n")
    joueur = input("Quel est votre choix ? ")
    print(" ")
    while(True):
        try: 
            if(int(joueur) not in [1, 2, 3, 4]):
                print("Veuillez saisir le chiffre correspondant à votre choix")
                joueur = input("Quel est votre choix ? ")
            else:
                break
        except ValueError:
            print("Veuillez saisir le chiffre correspondant à votre choix")
            joueur = input("Quel est votre choix ? ")
        print(" ")
    if(int(joueur) == 1):
        niveauColonne = 9
        niveauLigne = 9
        print("Vous avez choisie le niveau : Facile\n")
        jeu.logiqueJeu(niveauColonne, niveauLigne)
    elif(int(joueur) == 2):
        niveauColonne = 16
        niveauLigne = 16
        print("Vous avez choisie le niveau : Normal\n")
        jeu.logiqueJeu(niveauColonne, niveauLigne)
    elif(int(joueur) == 3):
        niveauColonne = 16
        niveauLigne = 30
        print("Vous avez choisie le niveau : Difficile\n")
        jeu.logiqueJeu(niveauColonne, niveauLigne)
    elif(int(joueur) == 4):
        accueil()



# Quitter
def quitter():
    pass


accueil()