from intersection_2_droites.intersection2droites import *
from equation_de_droite.droite import *
from maree.maree import *
from maree.func_maree import *
from convertisseur_de_coordonnees.coordonnee import *
from cascade_resultat.cascade_resultats import *
from json import *
from math import sqrt

with open('phare_de_France_dict.json') as json_data:  # on charge la liste des phare de france
    phare_de_france = load(json_data)

while True:
    print("""
1\Calcul de position
2\Calcul de cap
3\Calcul de maree
0\Quitter
""")
    answ = input("Que souhaitez vous faire?:")
    print("\n")
    try:
        answ = int(answ)
    except ValueError:
        print("impossible de rentrer autre chose que des chiffres (O, 1, 2 ,3)\nOn doit rentrer un chiffre en fonction de ce que l'on souhaite réaliser")

    if answ == 0:
        break
    elif answ == 1:
        while True:
            try:
                # a entrer a partir du moment où il y a des données en lat / long qui sont rentrée
                try :
                    if LCmin!=300:
                        pass
                    else:
                        print("-" * 40, sep="")
                        print("    Carte:")
                        LCmin = input("\t-latitude minimale : ")   # Pour l'émisphére Nord seulement et sans prendre en compte le passage de l'antiméridien
                        LCmax = input("\t-latitude maximale : ")
                        lCmin = input("\n\t-longitude minimale : ")
                        lCmax = input("\t-longitude maximale : ")
                    print("-" * 40, sep="")
                except NameError: 
                    print("-" * 40, sep="")
                    print("    Carte:")
                    LCmin = input("\t-latitude minimale : ")   # Pour l'émisphére Nord seulement et sans prendre en compte le passage de l'antiméridien
                    LCmax = input("\t-latitude maximale : ")
                    lCmin = input("\n\t-longitude minimale : ")
                    lCmax = input("\t-longitude maximale : ")
                    print("-" * 40, sep="")
                LCmin = float(LCmin)
                LCmax = float(LCmax)
                lCmin = float(lCmin)
                lCmax = float(lCmax)

                print("")
                distance_phare = []
                for phare in list(phare_de_france.keys()):
                    distance_phare.append(sqrt((abs(phare_de_france[phare][0] - abs(LCmax-LCmin)))*(abs(phare_de_france[phare][0] - abs(LCmax-LCmin))) + (abs(phare_de_france[phare][1] - abs(lCmax-lCmin)))*(abs(phare_de_france[phare][1] - abs(lCmax-lCmin)))))
                #print(sorted(distance_phare))
                print("Phare 1")
                choice = input(":")
                if 0 < choice < 10:
                    pass
                elif choice == 0:
                    break
                # a rentrer pour se localiser sur la carte (droite + intersection)
                else:
                    print("-" * 40, sep="")
                    print("    Phare 1:")
                    A1 = int(input("\t-angle de vision (°): "))
                    L1 = float(input("\n\t-latitude : "))
                    l1 = float(input("\t-longitude : "))
                    print("-" * 40, sep="")

                    print("")
                    print("-" * 40, sep="")
                    print("    Phare 2:")
                    A2 = int(input("\t-angle de vision (°): "))
                    L2 = float(input("\n\t-latitude : "))
                    l2 = float(input("\t-longitude : "))
                    print("-" * 40, sep="")
                    if A1 == A2 or A1 == A2+180 or A1+180 == A2:
                        print("\nimpossible de rentrer 2 angles équivalent à 180° prés\n")
                    else:
                        break

            except ValueError:
                print("""
Il faut rentrer les latitudes/longitude sous le format: hh.mmss,
et les angles de vision sous la forme: ddd (entre 0 et 360)
""")
                LCmin = 300
                LCmax = 0
                lCmin = 0
                lCmax = 0

        X1,Y1 = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin, L1, l1)
        X2,Y2 = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin, L2, l2)

        a1, b1, c1 = Droite(X1, Y1, A1)
        a2, b2, c2 = Droite(X2, Y2, A2)

        Xi, Yi = intersection(a1, b1, c1, a2, b2, c2)
        print("\n\nVotre position est :",Xi, Yi, "\n")

    elif answ == 2:
        choix()
    elif answ == 3:
        print("Calcul de maree")
        launch_marre()

print("A bientôt sur le super programme de calcul marin!!")


# programme qui nous localise sur une carte : 





