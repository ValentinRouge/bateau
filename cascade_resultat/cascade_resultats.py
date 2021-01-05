def reajustement(a):
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
    if a<0 : 
        a = 360 + a
    elif a > 360 : 
        a = a - 360
    return a

def CCtoCV(cc,d,a,D,b): 
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
    if a==1 :
        cm = cc + d
    else : 
        cm = cc - d
    if b == 1 : 
        cv = cm + D 
    else : 
        cv = cm -D
    result = reajustement(cv)
    return result


def CVtoCC(cv,d,a,D,b): 
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
    if a==1 :
        cm = cv - d
    else :
        cm = cv + d
    if b == 1 : 
        cc = cm - D 
    else : 
        cc = cm +D
    result = reajustement(cc)
    return result


def CVtoRS(cv,a): 
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
    rs = a+cv
    result = reajustement(rs)
    return result



def RStoCV(a,b) : 
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
    cv = a-b
    result = reajustement(cv)
    return result
    



def choix() : 
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
    print("que voulez vous faire ?")
    a = int(input("1- Cap compas => Cap vrai 2- Cap Vrai => cap compas 3- Route de surface => cap Vrai"))
    if a == 1 : 
        cc = int(input("Quel est le cap compas (en deg) ? "))
        d = int(input("Quel est la déviation ( en deg) ? "))
        a = int(input ("1 - Est 2 - West "))
        D = int(input("Quel est la déclinaison (en deg) ? "))
        b = int(input ("1 - Est 2 - West "))
        cv1 = CCtoCV(cc,d,a,D,b)
        print("le cap vrai est",cv1,"degrès")
        print("voulez vous calculer la route de Surface")
        b = int(input("1- oui 2- non"))
        if b == 1 : 
            cv = cv1
            a = int(input("Quelle est la valeur de la dérive (en deg)? "))
            print("la route de surface est", CVtoRS(cv,a),"degrès")          
    elif a == 2 :
        cv = int(input("Quel est le cap vrai (deg) ? "))
        d = int(input("Quel est la déviation ( en deg) ? "))
        a = int(input ("1 - Est 2 - West "))
        D = int(input("Quel est la déclinaison (en deg) ? "))
        b = int(input ("1 - Est 2 - West "))
        print("le cap compas est", CVtoCC (cv,d,a,D,b), "degrès")
    else  :
        cv2 = RStoCV(a,b)
        a = int(input("quelles est la valeur de la route de surface (en deg)? "))
        b= int(input("Quelle est la valeur de la dérive (en deg)? "))
        print("le cap vrai est",cv2,"degrès")
        print("voulez vous calculer le cap compas ?")
        c = int(input("1-oui 2- non "))
        if c == 1 :
            cv = cv2
            d = int(input("Quel est la déviation ( en deg) ? "))
            a = int(input ("1 - Est 2 - West "))
            D = int(input("Quel est la déclinaison (en deg) ? "))
            b = int(input ("1 - Est 2 - West "))
            print("le cap compas est", CVtoCC(cv,d,a,D,b),"degrès")

