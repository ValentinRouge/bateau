"""
Created on Tue Sep 15 14:13:50 2020

@author: Théotime

"""


def cap_compas () : 
    cc = int (input("Quel est le cap compas (en deg) ? "))
    return (cc)

def cap_vrai (): 
    cv = int (input("Quel est le cap vrai (deg) ? "))
    return (cv)

def deviation () :
    d = int ( input("Quel est la déviation ( en deg) ? "))
    return (d)
   
def orientation () : 
    a = int (input ("1 - Est 2 - West "))
    return (a)

def declinaison () : 
    D = int (input("Quel est la déclinaison (en deg) ? "))
    return (D)

def derive () :
    der = int (input("Quelle est la valeur de la dérive (en deg)? "))
    return (der)

def route_surface () : 
    RS = int(input ("quelles est la valeur de la route de surface (en deg)? "))
    return (RS)

def affichage_cv (a) : 
    print ("le cap vrai est ", a," degrès")

def affichage_cc (a) :
    print ("le cap compas est ", a," degrès")
    
def affichage_rs (a) :
    print ("la route de surface est",a,"degrès")

"""
    // ---------------- DEBUT EN TETE ---------------------------------------------------//
    // NOM :                    reajustement                                             //
    //                                                                                   //
    // AUTEURS : Théotime Poichotte                                                      //
    //                                                                                   //
    // VERSION :    1.0         Théotime Poichotte            septembre 2020             //
    //     Calcule la cascade de résultats                                               //
    // HISTORIQUE : Aucun                                                                //
    //                                                                                   //
    // ENTREES :                                                                         //
    //      a  	      valeur obtenues après la cascade de resultats		                 //
    //                                                                                   //
    //                                                                                   //    
    // SORTIES :                                                                         //
    //    valeur numérique d'un cap compris entre 0 et 360 °                             //
    //	               	                                                                 //
    // MODIFIEES :                                                                       //
    //    a                                                                              //
    // LOCALES :                                                                         //
    //    a                                                                              //
    //                                                                                   //
    // ALGO - REFERENCES :                                                               //
    //                                                                                   //
    //----------------- FIN EN TETE ---------------------------------------------------- //"""
def reajustement (a) :
    if a<0 : 
        a = 360 + a
    elif a > 360 : 
        a = a - 360
    return (a)

"""
 // ---------------- DEBUT EN TETE ------------------------------------------------------//
    // NOM :                   CCtoCV                                                    //
    //                                                                                   //
    // AUTEURS : Théotime Poichotte                                                      //
    //                                                                                   //
    // VERSION :    1.0         Théotime Poichotte            septembre 2020             //
    //     Calcule la cascade de résultats                                               //
    // HISTORIQUE : Aucun                                                                //
    //                                                                                   //
    // ENTREES :                                                                         //
    //     cc         cap compas                                                         //
    //     d          deviation                                                          //
    //     a          choix de l'utilisateur                                             //
    //     D          Declinaison                                                        //
    //     b		   choix del'utilisateur                                             //
    //                                                                                   //    
    // SORTIES :                                                                         //
    //     valeur du cap vrai                                                            //
    //                                                                                   //
    //                                                                                   //
    // MODIFIEES :                                                                       //
    //     cc        cap compas                                                          //
    //     cm        cap magnétique                                                      //
    //     cv        cap vrai                                                            //
    //                                                                                   //
    // LOCALES :                                                                         //
    //     cm        cap magnétique                                                      //
    //     cv        cap vrai                                                            //
    //                                                                                   // 
    //     FONCTIONS APPELEES :                                                          //
    //         reajustement                                                              //
    //                                                                                   //
    // ALGO - REFERENCES :                                                               //
    //                                                                                   //
    //----------------- FIN EN TETE -----------------------------------------------------//"""  
def CCtoCV (cc,d,a,D,b): 
    if a==1 :
        cm = cc + d
    else : 
        cm = cc - d
    if b == 1 : 
        cv = cm + D 
    else : 
        cv = cm -D
    result = reajustement(cv)
    return(result)

"""
 // ---------------- DEBUT EN TETE ------------------------------------------------------//
    // NOM :                    CVtoCC                                                   //
    //                                                                                   //
    // AUTEURS : Théotime Poichotte                                                      //
    //                                                                                   //
    // VERSION :    1.0         Théotime Poichotte            septembre 2020             //
    //     Calcule la cascade de résultats                                               //
    // HISTORIQUE : Aucun                                                                //
    //                                                                                   //
    // ENTREES :                                                                         //
    //     cv         cap vrai                                                           //
    //     d          deviation                                                          //
    //    a          choix de l'utilisateur                                              //
    //    D          Declinaison                                                         //
    //    b		   choix del'utilisateur        				                         //
    //                                                                                   //    
    // SORTIES :                                                                         //
    //     cap compas                                                                    //
    //	               	                                                                 //
    // MODIFIEES :                                                                       //
    //     cc        cap compas                                                          //
    //    cm        cap magnétique                                                       //
    //    cv        cap vrai                                                             //
    //                                                                                   //
    // LOCALES :                                                                         //
    //     cm        cap magnétique                                                      //
    //    cc        cap compas:                                                          //
    //                                                                                   //
    // FONCTIONS APPELEES :                                                              //
    //     reajustement                                                                  //
    //                                                                                   //
    // ALGO - REFERENCES :                                                               //
    //                                                                                   //
    //----------------- FIN EN TETE ---------------------------------------------------- //"""
def CVtoCC (cv,d,a,D,b) : 
    if a==1 :
        cm = cv - d
    else :
        cm = cv + d
    if b == 1 : 
        cc = cm - D 
    else : 
        cc = cm +D
    result = reajustement (cc)
    return (result)

"""
 // ---------------- DEBUT EN TETE ------------------------------------------------------//
    // NOM :                    CVtoRS                                                   //
    //                                                                                   //
    // AUTEURS : Théotime Poichotte                                                      //
    //                                                                                   //
    // VERSION :    1.0         Théotime Poichotte            septembre 2020             //
    //     Calcule la cascade de résultats                                               //
    // HISTORIQUE : Aucun                                                                //
    //                                                                                   //
    // ENTREES :                                                                         // 
    //     cv        cap vrai                                                            //
    //     a         valeur de la derive			                                     //
    //                                                                                   //    
    // SORTIES :                                                                         //
    //     valeur de la route de surface                                                 //
    //                                                                                   //
    // MODIFIEES :                                                                       //
    //     rs          route de surface                                                  //
    //                                                                                   //
    // LOCALES :                                                                         //
    //     cv        cap vrai                                                            //
    //     a         valeur de la derive                                                 //
    //                                                                                   //
    //    FONCTIONS APPELEES :                                                           //
    //         derive 	                                                                 //
    //                                                                                   //
    // ALGO - REFERENCES :                                                               //
    //                                                                                   //
    //----------------- FIN EN TETE -----------------------------------------------------//"""
def CVtoRS(cv,a) : 
    rs = a+cv
    result = reajustement(rs)
    return (result)


"""
 // ---------------- DEBUT EN TETE ------------------------------------------------------//
    // NOM :                    RStoCV                                                   //
    //                                                                                   //
    // AUTEURS : Théotime Poichotte                                                      //
    //                                                                                   //
    // VERSION :    1.0         Théotime Poichotte            septembre 2020             //
    //     Calcule la cascade de résultats                                               //
    // HISTORIQUE : Aucun                                                                //
    //                                                                                   //
    // ENTREES :                                                                         //
    //    a          route de surface                                                    //
    //     b          derive  				                                             //
    //                                                                                   //
    // SORTIES :                                                                         //
    //     valeur du cap vrai                                                            //
    //	               	                                                                 //
    // MODIFIEES :                                                                       //
    //     cv       cap vrai                                                             //
    //                                                                                   //
    // LOCALES :                                                                         //
    //     cv       cap vrai                                                             //  
    //                                                                                   //
    //     FONCTIONS APPELEES :                                                          //
    //         derive  	                                                                 //
    //         route_surface                                                             //
    //                                                                                   //
    // ALGO - REFERENCES :                                                               //
    //                                                                                   //
    //----------------- FIN EN TETE ---------------------------------------------------- 1//"""    
def RStoCV(a,b) : 
    cv = a-b
    result = reajustement(cv)
    return (result)
    

"""
 // ---------------- DEBUT EN TETE ------------------------------------------------------//
    // NOM :                    choix                                                //
    //                                                                                      //
    // AUTEURS : Théotime Poichotte                                                                    //
    //                                                                                      //
    // VERSION :    1.0         Théotime Poichotte            septembre 2020                        //
    //     Calcule la cascade de résultats                                     //
    // HISTORIQUE : Aucun                                                                   //
    //                                                                                      //
    // ENTREES :
cc = cap_compas()
        d         deviation
        a         orientation
        D         declinaison
        b         orientation 
        cv1       CCtoCV
        rs        CVtoRS
        cc        CVtoCC 			                                                            //
    //                     
    //                                                                                      //    
    // SORTIES :
    //    resultats de ce'quà demandé l'utilisateur                                                                            //
    //
    //    
    //    FONCTIONS APPELEES :
    //         deviation
    //        orientation
    //         declinaison
    //         orientation
    //         CCtoCV
    //        affichage_cv
    //      CVtoRS
    //         CVtoCC
    //        affichage_rs
    //         affichage_cc
    //         cap_vrai
    //         cap_compas
    //         route_surface
    //         derive
    //        RStoCV
    //
    //                                                                        //
    //                 
    //                                                                     //
    // ALGO - REFERENCES :                                                                  //
    //                                                                                      //
    //----------------- FIN EN TETE --------------------------------------------------------//"""
def choix() : 
    print ("que voulez vous faire ?")
    a = int(input ("1- Cap compas => Cap vrai 2- Cap Vrai => cap compas 3- Route de surface => cap Vrai"))
    if a == 1 : 
        cc = cap_compas()
        d = deviation()
        a = orientation()
        D = declinaison()
        b = orientation ()
        cv1 = CCtoCV(cc,d,a,D,b)
        affichage_cv(cv1)
        print ("voulez vous calculer la route de Surface")
        b = int(input("1- oui 2- non"))
        if b == 1 : 
            cv = cv1
            a = derive()
            rs = CVtoRS(cv,a)
            affichage_rs(rs)           
    elif a == 2 :
        cv = cap_vrai()
        d = deviation()
        a = orientation()
        D = declinaison()
        b = orientation ()
        cc = CVtoCC (cv,d,a,D,b)
        affichage_cc(cc)
    else  :
        a = route_surface()
        b= derive()
        cv2 = RStoCV (a,b)
        affichage_cv (cv2)
        print ("voulez vous calculer le cap compas ?")
        c = int (input ("1-oui 2- non "))
        if c == 1 :
            cv = cv2
            d = deviation()
            a = orientation()
            D = declinaison()
            b = orientation ()
            cc = CVtoCC (cv,d,a,D,b)
            affichage_cc(cc)

