import random
a=random.randint(0, 6)
def jouer(gril,j,col):
    compteur=0
    for i in range(6):
        if gril[5-i][a]==0 and compteur==0:
            gril[5-i][a]=j
            compteur+=1
    print (gril)


jouer([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]],2,1)
