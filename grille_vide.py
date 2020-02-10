def grille_vide():
    list_0=[0,0,0,0,0,0,0]
    list=[]
    for i in range(6):
        list.append(list_0)
    return list

assert grille_vide()==[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
