from intersection_2_droites.intersection2droites import *
from equation_de_droite.droite import *
from maree.maree import *
from convertisseur_de_coordonnees.coordonnee import *
from cascade_resultat.cascade_resultats import *

# a entrer a partir du moment où il y a des données en lat / long qui sont rentrée
LCmin = input("latitude minimale de la carte : ")
LCmax = input("latitude maximale de la carte : ")
lCmin = input("longitude minimale de la carte : ")
lCmax = input("longitude maximale de la carte : ")

# a rentrer pour se localiser sur la carte (droite + intersection)
A1 = input("angle de vision du premier phare : ")
L1 = input("latitude du premier phare : ")
l1 = input("longitude du premier phare : ")

A2 = input("angle de vision du second phare : ")
L2 = input("latitude du second phare : ")
l2 = input("longitude du second phare : ")

# programme qui nous localise sur une carte : 
X1,Y1 = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin, L1, l1)
X2,Y2 = convertDepuisLatLong(LCmax, LCmin, lCmax, lCmin, L2, l2)

Droite(X1, Y1, A1)
Droite(X2, Y2, A2)




