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

assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 1, 1, 1, 1, 0]],1,5)==True
assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]],1,5)==False





