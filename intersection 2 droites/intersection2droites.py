from numpy import * #pip install numpy

def intersection(a1,b1,c1,a2,b2,c2):
    """
    // ---------------- DEBUT EN TETE --------------------------------------//
    // NOM :                    intersection                                //
    //                                                                      //
    // AUTEURS : V Rouge                                                    //
    //                                                                      //
    // VERSION :    1.0         V Rouge               octobre 2020          //
    //     coordonnée d'un point d'intersection de deux droites             //
    // HISTORIQUE : Aucun                                                   //
    //                                                                      //
    // ENTREES :  				                                            //
    //	a1		X de la droite 1            	                            //
    //	b1 		Y de la droite 1                                            //
    //  c1      ordonée à l'origine de la droite 1    	                    //
    //	a2		X de la droite 2            	                            //
    //	b2 		Y de la droite 2                                            //
    //  c2      ordonée à l'origine de la droite 2    	                    //
    // SORTIES :                                                            //
    //	x : coordonnée en x                                         	    // 
    //  y : coordonnée en y                                                 //
    // MODIFIEES :                                                          //
    //                                                                      //
    // LOCALES :                                                            //
    //                                                                      //
    // FONCTIONS APPELEES :                                                 //
    //                                                                      //
    // ALGO - REFERENCES : numpy                                             //
    //                                                                      //
    // ---------------- FIN EN TETE ----------------------------------------//
    """
    A=matrix([[a1,b1],[a2,b2]])
    B=matrix([[-c1],[-c2]])
    solution=linalg.solve(A,B)
    return float(solution[0]),float(solution[1])
