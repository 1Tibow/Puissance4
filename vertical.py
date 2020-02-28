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
        
assert vert([[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [0, 0, 2, 0, 0, 0, 0],
      [0, 0, 2, 0, 0, 0, 0]],1,2,2)==False

assert vert([[0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 0, 2, 0, 1],
      [0, 1, 2, 2, 2, 1, 2],
      [0, 1, 1, 2, 2, 1, 2],
      [0, 2, 1, 1, 1, 2, 2]],2,2,4)==False