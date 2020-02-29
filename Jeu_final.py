#Il s'agit d'un programme permettant à deux personnes de jouer à une simulation du célèbre jeu : Puissance 4
#Pour lancer le jeu, il vous suffit de lancer le programme
#Il vous suffira alors de répondre à deux questions pour placer un jeton
#Il vous sera de suite afficher une grille avec votre jeton placé
#Puis laissez la deuxième personne répondre à son tour et ainsi de suite jusqu'à arriver à une situation final de jeu
#Bonne chance et amusez-vous

import random

def grille_vide():
    list=[]
    for i in range(6):
        list.append([0,0,0,0,0,0,0])
    return list

def coup_possible(gril,col):
    for i in range(6):
        if gril[i][col]==0:
            return True
    return False

def jouer(gril,j,col):
    compteur=0
    for i in range(6):
        if gril[5-i][col]==0 and compteur==0:
            gril[5-i][col]=j
            ligne=5-i
            compteur+=1
    return gril,ligne

def horiz (gril, j, lig):
    compteur=0
    for i in range(7):
        if gril[lig][i]==j:
            compteur+=1
            if compteur==4:
                return True
        else:
            compteur=0
    return False

def vert(gril,j,lig,col):
    verite=0
    if lig>2:
        return False
    for i in range(lig+1,lig+4):
        if gril[i][col]!=j:
            verite=1
    if verite==1:
        return False
    else:
        return True

def affiche(gril):
    print(" ","0","1","2","3","4","5","6")
    for i in range(6):
        print(i,end='')
        for z in range(7):
            if gril[i][z]==0:
                print("|.",end='')
            elif gril[i][z]==1:
                print("|x",end='')
            else:
                print("|0",end='')
            
        print("|")

def diag_haut(gril, j, lig, col):
    compteur=0
    liste_interdite=[[0,0],[0,1],[0,2],[1,0],[1,1],[2,0],[3,6],[4,5],[4,6],[5,4],[5,5],[5,6]]
    liste_1=[[3,0],[2,1],[1,2],[0,3]]
    liste_2=[[4,0],[3,1],[2,2],[1,3],[0,4]]
    liste_3=[[5,0],[4,1],[3,2],[2,3],[1,4],[0,5]]
    liste_4=[[5,1],[4,2],[3,3],[2,4],[1,5],[0,6]]
    liste_5=[[5,2],[4,3],[3,4],[2,5],[1,6]]
    liste_6=[[5,3],[4,4],[3,5],[2,6]]
    duo=[lig,col]
    if duo in liste_interdite:
        return False
    if duo in liste_1:
        for i in range(4):
            if gril[3-i][0+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_2:
        for i in range(5):
            if gril[4-i][0+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_3:
        for i in range(6):
            if gril[5-i][0+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_4:
        for i in range(6):
            if gril[5-i][1+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_5:
        for i in range(5):
            if gril[5-i][2+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_6:
        for i in range(4):
            if gril[5-i][3+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False

def diag_bas(gril, j, lig, col):
    compteur=0
    liste_interdite=[[0,4],[0,5],[0,6],[1,5],[1,6],[2,6],[3,0],[4,0],[4,1],[5,0],[5,1],[5,2]]
    liste_1=[[2,0],[3,1],[4,2],[5,3]]
    liste_2=[[1,0],[2,1],[3,2],[4,3],[5,4]]
    liste_3=[[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]]
    liste_4=[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]
    liste_5=[[0,2],[1,3],[2,4],[3,5],[4,6]]
    liste_6=[[0,3],[1,4],[2,5],[3,6]]
    duo=[lig,col]
    if duo in liste_interdite:
        return False
    if duo in liste_1:
        for i in range(4):
            if gril[2+i][0+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_2:
        for i in range(5):
            if gril[1+i][0+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_3:
        for i in range(6):
            if gril[0+i][0+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_4:
        for i in range(6):
            if gril[0+i][1+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_5:
        for i in range(5):
            if gril[0+i][2+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False
    if duo in liste_6:
        for i in range(4):
            if gril[0+i][3+i]==j:
                compteur+=1
                if compteur==4:
                    return True
            else:
                compteur=0
        return False

def match_nul(gril):
    for i in range(7):
        for z in range(6):
            if gril[z][i]==0:
                return False
    return True

def victoire(gril,j ,lig , col):
    if horiz(gril,j,lig)==True or diag_bas(gril,j,lig,col)==True or diag_bas(gril, j, lig, col)==True or vert(gril,j,lig,col)==True:
        return True
    else:
        return False

def coup_aleatoire(gril,j):
    a=random.randint(0, 6)
    compteur=0
    for i in range(6):
        if gril[5-i][a]==0 and compteur==0:
            gril[5-i][a]=j
            compteur+=1
    return gril

grille=grille_vide()
joueur=int(input("Quel est votre numéro de joueur ? ( 1 ou 2 ) "))
colonne=int(input("Dans quel colonne voulez-vous placer votre jeton ? "))
if coup_possible(grille,colonne)==True:
    grille,ligne=jouer(grille,joueur,colonne)
else:
    print("Coup impossible")
affiche(grille)
while victoire(grille,joueur,ligne,colonne)!=True and match_nul(grille)!=True:
    joueur=int(input("Quel est votre numéro de joueur ? ( 1 ou 2 ) "))
    colonne=int(input("Dans quel colonne voulez-vous placer votre jeton ? "))
    if coup_possible(grille,colonne)==True:
        grille,ligne=jouer(grille,joueur,colonne)
    else:
        print("Coup impossible")
    affiche(grille)
if victoire(grille,joueur,ligne,colonne)==True:
    print("Le joueur",joueur,"a gagné ! Bien joué !")
if match_nul(grille)==True:
    print("Dommage, c'est une égalité")