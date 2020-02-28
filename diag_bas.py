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

assert diag_bas([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0]],1,2,1)==True
assert diag_bas([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]],1,2,2)==False










