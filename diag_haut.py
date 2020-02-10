
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

assert diag_haut([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]],1,5,2)== True
assert diag_haut([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]],1,5,2)==False


