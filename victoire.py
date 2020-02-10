def victoire(gril,j ,lig , col):
    if horiz(gril,j,lig , col)==True or diag_bas(gril,j,lig,col)==True or diag_bas(gril, j, lig, col)==True or vert(gril,j,lig,col) :
        return True
    else:
        return False

assert victoire([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0]],1,5,2)== True

