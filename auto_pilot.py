from intersection_2_droites.intersection2droites import *
from equation_de_droite.droite import *
from maree.maree import *
from maree.func_maree import *
from convertisseur_de_coordonnees.coordonnee import *
from cascade_resultat.cascade_resultats import *
from json import *
from math import sqrt
from phare_de_france.new_phare import *


def calcul_de_pos():
    """
    Permet de lancer le calcul de position tout en proposant d'utiliser des phares présents dans le fichier 'phare_de_france\phare_de_France_dict.json'
    """
    #donnée
    with open('phare_de_france\phare_de_France_dict.json') as json_data:  # on charge la liste des phare de france
        phare_de_france = load(json_data)

    while True:
        try:
            # a entrer a partir du moment où il y a des données en lat / long qui sont rentrée
            try :
                if LCmin!=300:  # On essaie de voir si on a déja les dimension de la carte
                    pass
                else:  # si on a causé une erreur d'input en ayant pas les dimensions de la carte
                    print("-" * 40, sep="")
                    print("    Carte:")
                    LCmin = input("\t-latitude minimale : ")
                    LCmax = input("\t-latitude maximale : ")
                    lCmin = input("\n\t-longitude minimale : ")
                    lCmax = input("\t-longitude maximale : ")
                print("-" * 40, sep="")
            except NameError:  # si on a pas les dimensions de la carte
                print("-" * 40, sep="")
                print("    Carte:")
                LCmin = input("\t-latitude minimale : ")   # Pour l'émisphére Nord seulement et sans prendre en compte le passage de l'antiméridien
                LCmax = input("\t-latitude maximale : ")
                lCmin = input("\n\t-longitude minimale : ")
                lCmax = input("\t-longitude maximale : ")
                print("-" * 40, sep="")
            LCmin = float(LCmin)  # on vérifie le type des valeurs, sinon cela cause une value error récup plus bas
            LCmax = float(LCmax)
            lCmin = float(lCmin)
            lCmax = float(lCmax)

            print("")
            distance_phare = []
            for phare in list(phare_de_france.keys()):  # on récupère une liste des distances des phare au centre de la carte
                distance_phare.append(sqrt((abs(phare_de_france[phare][0] - abs(LCmax-LCmin)))*(abs(phare_de_france[phare][0] - abs(LCmax-LCmin))) + (abs(phare_de_france[phare][1] - abs(lCmax-lCmin)))*(abs(phare_de_france[phare][1] - abs(lCmax-lCmin)))))
            for i in range(1, 3):
                while True:
                    while True:
                        print("\nPhare", i)
                        print("0-Quitter")
                        for j in range(8):
                            phare = list(phare_de_france.keys())[distance_phare.index(sorted(distance_phare)[j])]
                            print("{}-{} ({}, {})".format(j+1, phare.ljust(30), str(phare_de_france[phare][0]).ljust(9), str(phare_de_france[phare][1]).ljust(10)))
                        print("9-rechercher un phare")
                        print("10-Rentrer à la main les positions du phare")
                        try:
                            choice = int(input(":"))
                            break
                        except ValueError:  # si on rentre autre chose qu'un nombre
                            print("il faut rentrer un nombre")
                    if 0 < choice < 9:  # si compris entre 1 et 9 (si on choisit un des phares proches)
                        if i == 1:
                            A1 = int(input("\t-angle de vision (°): "))  # on choisi l'angle du phare 1
                            L1 = float(phare_de_france[list(phare_de_france.keys())[distance_phare.index(sorted(distance_phare)[choice-1])]][0])
                            l1 = float(phare_de_france[list(phare_de_france.keys())[distance_phare.index(sorted(distance_phare)[choice-1])]][1])
                        else:
                            A2 = int(input("\t-angle de vision (°): "))  # on choisi l'angle du phare 2
                            L2 = float(phare_de_france[list(phare_de_france.keys())[distance_phare.index(sorted(distance_phare)[choice-1])]][0])
                            l2 = float(phare_de_france[list(phare_de_france.keys())[distance_phare.index(sorted(distance_phare)[choice-1])]][1])
                        break
                    elif choice == 9:  # si on veut rechercher un phare par son nom
                        nom = input("entrez un nom de phare : ")
                        liste_recherche = []
                        for phare in list(phare_de_france.keys()):
                            for letter in range(len(nom)):
                                if nom[letter] == phare[letter]:  # on compare ce qu'on a entré avec le débuty du nom des phares
                                    pass
                                else:
                                    break
                                if letter + 1 == len(nom):  # si ils sont identiques pour toutes les lettres on l'ajoute à la liste
                                    liste_recherche.append(phare)
                        while True:
                            print("0-Retour")
                            for j in range(len(liste_recherche)):  # on affiche la liste des phares qui commence par ce qu'on a rentré
                                print("{}-{} ({}, {})".format(str(j+1), str(liste_recherche[j]).ljust(30), str(phare_de_france[str(liste_recherche[j])][0]).ljust(9), str(phare_de_france[str(liste_recherche[j])][1]).ljust(10)))
                            try:
                                select = int(input(":"))  # on séléctionne un phare en particulier
                                if select == 0:
                                    break
                                elif 0 < select <= len(liste_recherche):
                                    if i == 1:
                                        A1 = int(input("\t-angle de vision (°): "))  # on choisi l'angle du phare 1
                                        L1 = float(phare_de_france[str(liste_recherche[select-1])][0])
                                        l1 = float(phare_de_france[str(liste_recherche[select-1])][1])
                                    else:
                                        A2 = int(input("\t-angle de vision (°): "))  # on choisi l'angle du phare 2
                                        L2 = float(phare_de_france[str(liste_recherche[select-1])][0])
                                        l2 = float(phare_de_france[str(liste_recherche[select-1])][1])
                                    break
                                else:
                                    print("Il faut rentrer un des nombre affiché")
                            except ValueError:
                                print("il faut rentrer un nombre")
                        if select != 0:
                            break
                    elif choice == 0:  # si on choisit 0 cela arréte la boucle
                        break
                    # a rentrer pour se localiser sur la carte (droite + intersection)
                    else:
                        print("")
                        if i == 1:
                            print("-" * 40, sep="")  # affichage
                            print("    Phare 1:")  # affichage
                            A1 = int(input("\t-angle de vision (°): "))  # on choisi l'angle du phare 1
                            print("\n\tVeuillez entrer les cordonnées au format XX,XXXXXX")
                            L1 = float(input("\t-latitude : "))  # latitude
                            l1 = float(input("\t-longitude : "))  # longitude
                            print("-" * 40, sep="")  # affichage
                            phare_de_france = new_phare(L1,l1)
                            break
                        else:
                            print("-" * 40, sep="")
                            print("    Phare 2:")
                            A2 = int(input("\t-angle de vision (°): "))  # on choisi l'angle du phare 2
                            print("\n\tVeuillez entrer les cordonnées au format XX,XXXXXX")
                            L2 = float(input("\t-latitude : "))
                            l2 = float(input("\t-longitude : "))
                            print("-" * 40, sep="")
                            phare_de_france = new_phare(L2,l2)

                            break
            if choice == 0:  # pour revenir au menu principal
                break
            elif A1 == A2 or A1 == A2+180 or A1+180 == A2:  # si les droite sont paralélles
                print("\nimpossible de rentrer 2 angles équivalent à 180° prés\n")
            else:
                break

        except ValueError:  # si on a pas rentrer les bons type pour une ou plusieurs données
            print("""
Il faut rentrer les latitudes/longitude sous le format: hh.mmss,
et les angles de vision sous la forme: ddd (entre 0 et 360)
""")
            LCmin = 300
            LCmax = 0
            lCmin = 0
            lCmax = 0

    if choice == 0:  # pour revenir au menu principal
        pass
    else:
        Xcoef,Ycoef = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin)
        X1,Y1 = LltoXY(L1, l1, Xcoef,Ycoef,LCmin,lCmin)  # conversion des données
        X2,Y2 = LltoXY(L2, l2, Xcoef,Ycoef,LCmin,lCmin)

        a1, b1, c1 = Droite(X1, Y1, A1)  # calcul des droites
        a2, b2, c2 = Droite(X2, Y2, A2)

        Xi, Yi = intersection(a1, b1, c1, a2, b2, c2)  # intersection des droites
        LP,lp = XYtoLl(Xi,Yi,Xcoef,Ycoef,LCmin,lCmin)
        print("\n\nVotre position est :",LP, lP, "\n")  # affichage final



#début du menu principal
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
        calcul_de_pos()
    elif answ == 2:
        choix()
    elif answ == 3:
        print("Calcul de maree")
        launch_marre()
print("A bientôt sur le super programme de calcul marin!!")
