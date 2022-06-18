from math import *

is_start_ready = 'true'
n = int(input("entrer la taille de l'image : "))
if n%2 == 0:
    print('Nombre invalide')
    is_start_ready = 'false'
else:
    is_start_ready = 'true'

    
tableau = []
premier = []
file = open('resultat.pbm', 'w')
file.write("P1\n")
file.write(str(n) + " " + str(n) + "\n")
centre = int(n/2)



#fonctions


def crible_eratostene(iteration):
    for x in range(2, (iteration*iteration)+1):
        marqueur = 1
        for k in range (2,int(sqrt(x))*2):
            if x%k==0:
                marqueur=0
        if marqueur==0:
           pass
        else:
            premier.append(x)


def creer_un_tableau():
    for x in range(n):
        tableau.append(['0']*n)



#création de la spirale*********************************************
spirale = []
for x in range(n):
    spirale.append('0'*n)



#valeurs initiales
def generation_val_init(image_size):
    coordx = int(image_size/2)
    coordy = int(image_size/2)
    unite = 1
    return coordx, coordy, unite



#fonction spirale
def creer_spirale(interation):
    coordx, coordy, unite = generation_val_init(n)
    for x in range(1, interation, 2):
        coordx, coordy, unite = boucle_forward(x, coordx, coordy, unite)
        coordx, coordy, unite = boucle_up(x, coordx, coordy, unite)
        coordx, coordy, unite = boucle_back(x+1, coordx, coordy, unite)
        coordx, coordy, unite = boucle_down(x+1, coordx, coordy, unite)
    coordx, coordy, unite = boucle_forward(n-1, coordx, coordy, unite)



#coordonnées
def calcul_coordx(arret, is_true_false):
    if is_true_false == 'plus':
        arret += 1
    elif is_true_false == 'moins':
        arret -= 1
    else:
        pass
    return arret


def calcul_coordy(arret, is_true_false):
    if is_true_false == 'plus':
        arret += 1
    elif is_true_false == 'moins':
        arret -= 1
    else:
        pass
    return arret



#fonctions de directions
def forward(coordx, coordy, unite):
    coordx = calcul_coordx(coordx, 'plus')
    coordy = calcul_coordy(coordy, 'neutre')
    val = increment(unite)
    if val in premier:
        tableau[coordy][coordx] = '1'
    return coordx, coordy, val


def up(coordx, coordy, unite):
    coordx = calcul_coordx(coordx, 'neutre')
    coordy = calcul_coordy(coordy, 'moins')
    val = increment(unite)
    if val in premier:
        tableau[coordy][coordx] = '1'
    return coordx, coordy, val

    
def back(coordx, coordy, unite):
    coordx = calcul_coordx(coordx, 'moins')
    coordy = calcul_coordy(coordy, 'neutre')
    val = increment(unite)
    if val in premier:
        tableau[coordy][coordx] = '1'
    return coordx, coordy, val


def down(coordx, coordy, unite):
    coordx = calcul_coordx(coordx, 'neutre')
    coordy = calcul_coordy(coordy, 'plus')
    val = increment(unite)
    if val in premier:
        tableau[coordy][coordx] = '1'
    return coordx, coordy, val



#incrémentation de la valeur
def increment(nb):
    nb += 1
    return nb



#boucles de génération
def boucle_forward(number, coordx, coordy, unite):
    for x in range(number):
        coordx, coordy, unite = forward(coordx, coordy, unite)
    return coordx, coordy, unite


def boucle_up(number, coordx, coordy, unite):
    for x in range(number):
        coordx, coordy, unite = up(coordx, coordy, unite)
    return coordx, coordy, unite


def boucle_back(number, coordx, coordy, unite):
    for x in range(number):
        coordx, coordy, unite = back(coordx, coordy, unite)
    return coordx, coordy, unite


def boucle_down(number, coordx, coordy, unite):
    for x in range(number):
        coordx, coordy, unite = down(coordx, coordy, unite)
    return coordx, coordy, unite
    


#********************************************************************
def creer_image():
    for x in range(n):
        file.write(" ".join(tableau[x]))
        file.write("\n")



#programme principal
if is_start_ready == 'true':
    creer_un_tableau()
    crible_eratostene(n)
    creer_spirale(n)
    creer_image()
else:
    pass
file.close()
