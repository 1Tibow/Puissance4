def match_nul(gril):
    for i in range(7):
        for z in range(6):
            if gril[z][i]==0:
                return False
    return True

assert match_nul([[1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 2, 1, 1, 1, 1],
 [1, 2, 1, 2, 1, 2, 1]])== True
assert match_nul([[1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1],
 [1, 1, 2, 1, 0, 1, 1],
 [1, 2, 1, 2, 1, 2, 1]])== False


