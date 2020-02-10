
def affiche(gril):
    """ Affichage textye de la grille
    """
    print(" ","0","1","2","3","4","5","6")
    for i in range(6):
        print(i,end='')
        for z in range(7):
            if gril[i][z]==0:
                print("|.",end='')
            elif gril[i][z]==1:
                print("|x",end='')
            else:
                print("|0",end='')
            
        print("|")   
    
affiche([[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 2, 0, 0],
         [0, 0, 1, 0, 2, 0, 0],
         [0, 0, 1, 0, 2, 0, 0]]) 
    

