def grille_vide():
    list_0=[0,0,0,0,0,0,0]
    list=[]
    for i in range(6):
        list.append(list_0)
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
            compteur+=1
    return gril

def horiz (gril, j, lig, col):
    compteur=0
    if lig>5:
        return False
    if col>3:
        return False
    for i in range(4):
        if gril[lig][col+i]==j:
            compteur+=1
    if compteur==4:
            return True
    return False

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
    if lig<4:
        return False
    if col>2:
        return False
    for i in range(4):
        if gril[lig-i][col+i]==j:
            compteur+=1
    if compteur==4:
            return True
    return False

def diag_bas(gril, j, lig, col):
    compteur=0
    if lig>3:
        return False
    if col>2:
        return False
    for i in range(4):
        if gril[lig+i][col+i]==j:
            compteur+=1
    if compteur==4:
            return True
    return False

def match_nul(gril):
    for i in range(7):
        for z in range(6):
            if gril[z][i]==0:
                return False
    return True

def victoire(gril,j ,lig , col):
    if horiz(gril,j,lig , col)==True or diag_bas(gril,j,lig,col)==True or diag_bas(gril, j, lig, col)==True or vert(gril,j,lig,col) :
        return True
    else:
        return False
