from math import *


def convertDepuisLatLong(latMaxCarte, latMinCarte, longMaxCarte, longMinCarte):
    """
    // ---------------- DEBUT EN TETE --------------------------------------//
    // NOM :                    convertDepuisLatLong                        //
    //                                                                      //
    // AUTEURS : V Rouge                                                    //
    //                                                                      //
    // VERSION :    1.0         V Rouge               novembre  2020        //
    //     transforme coordonnées en latitude longitude en cartésienne sur  //
    // sur l'intervalle d'une carte                                         //
    // HISTORIQUE : Aucun                                                   //
    //                                                                      //
    // ENTREES :  				                                            //
    //	latMaxCarte		latitude maximale de la carte                       //
    //	latMinCarte		latitude minimale de la carte                       //
    //	longMaxCarte		longitude maximale de la carte                  //
    //	longMinCarte		longitude minimale de la carte                  //
    //  lat             latitude de la carte                                //
    //  long            longiude maximale de la carte                       //
    // SORTIES :                                                            //
    //	X : coordonée en X du point sur la carte                      	    // 
    //  Y : coordonnée en Y du point sur la carte                           //
    // MODIFIEES :                                                          //
    //                                                                      //
    // LOCALES :                                                            //
    //                                                                      //
    // FONCTIONS APPELEES :                                                 //
    //    convertLatLongXY()                                                //
    // ALGO - REFERENCES :                                                  //
    //     math                                                             //
    //                                                                      //
    // ---------------- FIN EN TETE ----------------------------------------//
    """

    Xmin,Ymin = convertLatLongXY(latMinCarte, longMinCarte)
    Xmax,_ = convertLatLongXY(latMinCarte, longMaxCarte)
    _,Ymax = convertLatLongXY(latMaxCarte, longMinCarte)
    Xcarte = Xmax - Xmin
    Ycarte = Ymax - Ymin


    Xcoef = 100/Xcarte
    Ycoef = 100/Ycarte

    return Xcoef, Ycoef

def LltoXY(lat, long, Xcoef, Ycoef, latMinCarte,longMinCarte):
    Xmin,Ymin = convertLatLongXY(latMinCarte, longMinCarte)
    Xpos,Ypos = convertLatLongXY(lat,long)

    Xresultat = (Xpos-Xmin) * Xcoef
    Yresultat = (Ypos-Ymin) * Ycoef

    return Yresultat,Xresultat

def XYtoLl(X, Y, Xcoef, Ycoef, latMinCarte, longMinCarte):
    Xmin,Ymin = convertLatLongXY(latMinCarte, longMinCarte)

    Ypos = Y/Xcoef+Ymin
    Xpos = X/Ycoef+Xmin

    R=6371
    Lat = float(Lat)
    Long = float(Long)

    return Ypos/R, Xpos/(R * cos(radians(Ypos/R)))


def convertLatLongXY(Lat, Long):
    """
    // ---------------- DEBUT EN TETE --------------------------------------//
    // NOM :                    convertLatLongXY                            //
    //                                                                      //
    // AUTEURS : V Rouge                                                    //
    //                                                                      //
    // VERSION :    1.0         V Rouge               novembre  2020        //
    //     convertit une coordonnée sphérique en cartésien                  //
    // HISTORIQUE : Aucun                                                   //
    //                                                                      //
    // ENTREES :  				                                            //
    //  lat             latitude du point                                   //
    //  long            longiude du point                                   //
    // SORTIES :                                                            //
    //	X : coordonée en X du point                                   	    // 
    //  Y : coordonnée en Y du point                                        //
    // MODIFIEES :                                                          //
    //                                                                      //
    // LOCALES :                                                            //
    //                                                                      //
    // FONCTIONS APPELEES :                                                 //
    // ALGO - REFERENCES :                                                  //
    //     math                                                             //
    //                                                                      //
    // ---------------- FIN EN TETE ----------------------------------------//
    """
    R=6371
    Lat = float(Lat)
    Long = float(Long)

    return R * Long * cos(radians(Lat)), R * Lat



"""Xm = "47°35'70" #input("Latmax")
xm = "47°15'50" #input("Latmin")
Ym = "3°10'00" #input("Longmax")
ym = "2°27'30" #input("Longmin")
x = "47°25'30" #input("Latpos")
y = "2°50'00" #input("Longpos")"""
