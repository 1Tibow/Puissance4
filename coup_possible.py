def coup_possible(gril,col):
    for i in range(6):
        if gril[i][col]==0:
            return True
    return False

assert coup_possible([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 0, 0]],2)== True
assert coup_possible([[0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0]],4)== False


