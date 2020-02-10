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










