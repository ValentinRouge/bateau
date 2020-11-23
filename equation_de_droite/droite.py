import math

def Droite(Xpoint,Ypoint,angle):
    """
    // ---------------- DEBUT EN TETE --------------------------------------//
    // NOM :                    Droite                                      //
    //                                                                      //
    // AUTEURS : V Rouge                                                    //
    //                                                                      //
    // VERSION :    1.0         V Rouge               septembre 2020        //
    //     Equation d'une droite a partir un point et un angle              //
    // HISTORIQUE : Aucun                                                   //
    //                                                                      //
    // ENTREES :  				                                            //
    //	Xpoint		position en X            	                            //
    //	Ypoint 		position en Y            	                            //
    //  angle       angle en degré par rapport à la verticale               //     
    // SORTIES :                                                            //
    //	a : coefficient devant le x, égal à moins la pente            	    // 
    //  b : coefficient devant le y, 1 sauf si la droite est verticale      //
    //  c : moins ordonnée à l'origine                                      //
    // MODIFIEES :                                                          //
    //                                                                      //
    // LOCALES :                                                            //
    //                                                                      //
    // FONCTIONS APPELEES :                                                 //
    //                                                                      //
    // ALGO - REFERENCES :                                                  //
    //                                                                      //
    // ---------------- FIN EN TETE ----------------------------------------//
    """
    Xpoint=int(Xpoint)
    Ypoint=int(Ypoint)
    angle = int(angle)
    
    if angle == 0 or angle == 360 or angle == 180:
        a = 1
        b = 0
        c = - Xpoint 

    elif angle == 90 or angle == 270:
        a = 0 
        y = 1
        c = - Ypoint
        
    elif angle > 0 and angle < 90:
        pente = round(math.tan(math.radians(90-angle)),3)
        ordOrigine = round(Ypoint - pente * Xpoint,3)
        a = - pente
        b = 1
        c = -ordOrigine

    elif angle > 90 and angle < 180:
        pente = round(math.tan(math.radians(90-angle)),3)
        ordOrigine = round(Ypoint - pente * Xpoint,3)
        a = - pente
        b = 1
        c = -ordOrigine 

    elif angle > 180 and angle < 270:
        pente = round(math.tan(math.radians(90-angle)),3)
        ordOrigine = round(Ypoint - pente * Xpoint,3)
        a = - pente
        b = 1
        c = -ordOrigine

    elif angle > 270 and angle < 360:
        pente = round(math.tan(math.radians(90-angle)),3)
        ordOrigine = round(Ypoint - pente * Xpoint,3)
        a = - pente
        b = 1
        c = -ordOrigine

    return a,b,c

