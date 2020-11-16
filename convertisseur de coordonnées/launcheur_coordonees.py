from coordonnee import *
from math import *


def convertirLatLongChiffre(L):
    """
    // ---------------- DEBUT EN TETE --------------------------------------//
    // NOM :                    convertir LatLongChiffre                    //
    //                                                                      //
    // AUTEURS : V Rouge                                                    //
    //                                                                      //
    // VERSION :    1.0         V Rouge               novembre  2020        //
    //     transforme coordonnées en latitude longitude en cartésienne sur  //
    // sur l'intervalle d'une carte                                         //
    // HISTORIQUE : Aucun                                                   //
    //                                                                      //
    // ENTREES :  				                                            //
    //	L		longitude ou latitude en degrés  (XX°XX'XX)                 //
    // SORTIES :                                                            //
    //	même chose en version numérique (XX,XXXX)                      	    // 
    // MODIFIEES :                                                          //
    //                                                                      //
    // LOCALES :                                                            //
    //                                                                      //
    // FONCTIONS APPELEES :                                                 //
    // ALGO - REFERENCES :                                                  //
    //                                                                      //
    // ---------------- FIN EN TETE ----------------------------------------//
    """
    d, m = L.split("°")
    m, s = m.split("'")
    return int(d) + int(m)/100 + int(s)/10000


Xm = convertirLatLongChiffre(input("Latitude maximale\n:"))
xm = convertirLatLongChiffre(input("Latitude miminmale\n:"))
Ym = convertirLatLongChiffre(input("Longitude maximale\n:"))
ym = convertirLatLongChiffre(input("Longitude minimale\n:"))
x = convertirLatLongChiffre(input("Latitude actuelle\n:"))
y = convertirLatLongChiffre(input("Longitude actuelle\n:"))
print(convertDepuisLatLong(Xm, xm, Ym, ym, x, y))