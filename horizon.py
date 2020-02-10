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

assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0]],1,5,2)==True
assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]],1,5,2)==False





