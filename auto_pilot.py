from intersection_2_droites.intersection2droites import *
from equation_de_droite.droite import *
from maree.maree import *
from maree.launcheur_maree import *
from convertisseur_de_coordonnees.coordonnee import *
from cascade_resultat.cascade_resultats import *

while True:
    print("""
1\Calcul de position
2\Calcul de cap
3\Calcul de maree
0\Quitter
""")
    answ = input("Que souhaitez vous faire?\n:")
    print("\n")
    try:
        answ = int(answ)
    except ValueError:
        print("impossible de rentrer autre chose que des chiffres (O, 1, 2 ,3)\nOn doit rentrer un chiffre en fonction de ce que l'on souhaite réaliser")

    if answ == 0:
        break
    elif answ == 1:
        # a entrer a partir du moment où il y a des données en lat / long qui sont rentrée
        try :
            LCmin==0
        except : 
            LCmin = input("latitude minimale de la carte : ")
            LCmax = input("latitude maximale de la carte : ")
            lCmin = input("longitude minimale de la carte : ")
            lCmax = input("longitude maximale de la carte : ")

        # a rentrer pour se localiser sur la carte (droite + intersection)
        A1 = input("angle de vision du premier phare : ")
        X1 = input("latitude du premier phare : ")
        Y1 = input("longitude du premier phare : ")

        A2 = input("angle de vision du second phare : ")
        X2 = input("latitude du second phare : ")
        Y2 = input("longitude du second phare : ")

        #X1,Y1 = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin, L1, l1)
        #X2,Y2 = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin, L2, l2)

        a1, b1, c1 = Droite(X1, Y1, A1)
        a2, b2, c2 = Droite(X2, Y2, A2)

        Xi, Yi = intersection(a1, b1, c1, a2, b2, c2)
        print(Xi, Yi)

    elif answ == 2:
        try :
            LCmin==0
        except : 
            LCmin = input("latitude minimale de la carte : ")
            LCmax = input("latitude maximale de la carte : ")
            lCmin = input("longitude minimale de la carte : ")
            lCmax = input("longitude maximale de la carte : ")
    elif answ == 3:
        print("Calcul de maree")
        lauch_marre()


# programme qui nous localise sur une carte : 





