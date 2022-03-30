import random
from tkinter import *

grille = []
b = []

# grille
def creationGrille(window, niveauColonne, niveauLigne, mines):
    
    canva = Canvas(window, width=300, height=300, bg='#2515AA')
    numCase = 0
    maxCase = niveauColonne * niveauLigne -1
    for i in range(niveauColonne):
        for j in range(niveauLigne):
            grille.append(Label(canva, text=" ", bd=1, width=1, height=1,padx=9,pady=5, relief=SUNKEN))
            grille[numCase].grid(row=j, column=i)

            b.append(Button(canva,text="",image="",padx=8,pady=1)) 
            b[numCase].grid(row=j, column=i)
            b[numCase].bind("<Button-1>", lambda i, coord=numCase: click(grille, b, coord))
            b[numCase].config(relief=RAISED)
            numCase +=1
    coordsMines(grille, maxCase, numCase, mines)
    canva.pack()
    
#  Chiffres
def chiffres(ref, niveauColonne, niveauLigne, maxCase):

    maxBomb=["1","2","3","4","5","6","7","8"]
    top=[]
    down=[]
    top.append(0)
    for i in range(niveauLigne):
        top.append((i+1)*niveauColonne)
        down.append(((i+1)*niveauColonne)-1)
    down.append(niveauColonne * niveauLigne)

    if ref in top:
        for i in [ref-niveauLigne,ref-(niveauLigne-1),ref+niveauLigne,ref+(niveauLigne+1),ref+1]:  #On parcours les positions à côter de la bombe pour mettre si possible les bombes à proximités pour le HAUT
            if i>=0 and i<=maxCase:
                if grille[i].cget("text")==" ":
                    v="1"
                elif grille[i].cget("text") in maxBomb:
                    v=str(int(grille[i].cget("text"))+1)
                grille[i].config(text=v)
    elif ref in down:
        for i in [ref-niveauLigne,ref-(niveauLigne+1),ref+niveauLigne,ref+(niveauLigne-1),ref-1]:  #On parcours les positions à côter de la bombe pour mettre si possible les bombes à proximités pour le BAS
            if i>=0 and i<=maxCase:
                if grille[i].cget("text")==" ":
                    v="1"
                elif grille[i].cget("text") in maxBomb:
                    v=str(int(grille[i].cget("text"))+1)
                grille[i].config(text=v)
    else:
        for i in [ref-niveauLigne,ref-(niveauLigne+1),ref-(niveauLigne-1),ref+niveauLigne,ref+(niveauLigne-1),ref+(niveauLigne+1),ref-1,ref+1]:  #On parcours les positions à côter de la bombe pour mettre si possible les bombes à proximités pour les autres
            if i>=0 and i<=maxCase:
                if grille[i].cget("text")==" ":
                    v="1"
                elif grille[i].cget("text") in maxBomb:
                    v=str(int(grille[i].cget("text"))+1)
                grille[i].config(text=v)
                
# photo= PhotoImage(file="img/bombe.png")

# mines

def click(grille, b, coord):
    b[coord].grid_forget()
    verifGagne(grille, coord)

def coordsMines(grille, maxCase, numCase, mines):
    presenceBombe = []
    
    for i in range(mines):
        nb1 = random.randint(0, maxCase)
        while nb1 in presenceBombe:
                nb1 = random.randint(0, maxCase)
        presenceBombe.append(nb1)
        grille[nb1].config(text="B", relief = GROOVE, bd=1,width=0,height=0)
        presenceBombe.append(numCase)

def verifGagne(grille, coord):
    if grille[coord].cget("text") == "B":
        perdu()

def perdu():
    
    perdu = Tk()
    perdu.title("Démineur")
    perdu.config(bg="#2515AA")
    messagePerdu = Text(perdu, text = "BOUM! Vous avez perdu.", fg="Arial, 10")
    messagePerdu.pack(expand=CENTER)
    perdu.mainloop()


# def supprimer(b, coord):
#     maxCase = len(coord)
#     for i in maxCase:
#         b[i].grid_forget()