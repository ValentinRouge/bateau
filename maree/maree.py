def TideLevel(MinHour, MaxHour, MinLevel, MaxLevel, Var):
    """
        // ---------------- DEBUT EN TETE ------------------------------------------------------//
        // NOM :                    TideLevel                                                   //
        //                                                                                      //
        // AUTEURS : JB Moufle                                                                  //
        //                                                                                      //
        // VERSION :    1.0         JB Moufle               28/09/2020                          //
        //     Calcule le niveau de la marée a toute heure                                      //
        // HISTORIQUE : Aucun                                                                   //
        //                                                                                      //
        // ENTREES :  				                                                            //
        //	MinHour 		tuple de la forme (HH,MM) de l'heure de début de marée            	//
        //	MaxHour 		tuple de la forme (HH,MM) de l'heure de fin de marée                //
        //  MinLevel        float du niveau d'eau au début de la marée                          //
        //  MaxLevel        float du niveau d'eau a la fin de la marée                          //
        //	Var		        tuple de la forme (HH,MM) de l'heure a laquelle on veut le niveau   //
        //                                                                                      //
        // SORTIES :                                                                            //
        //	float du niveau d'eau à l'heure demandée                   	                        //
        // MODIFIEES :                                                                          //
        //                                                                                      //
        // LOCALES :                                                                            //
        //    MinHour 		    int de l'heure de début de marée en minute           	        //
        //	  MaxHour 		    int de l'heure de fin de marée en minute                        //
        //    MinLevel          float du niveau d'eau au début de la marée                      //
        //    MaxLevel          float du niveau d'eau a la fin de la marée                      //
        //	  Var		        int de l'heure de marée en minute dont on cherche la hauteur    //
        //    TideHour          int correspondant à la durée en minute de l'heure marée         //
        //    TideHour6         float correspondant à la durée en minute d'1/12 de l'heure marée//
        //    WaterElevation    float qui contient l'élévation totale de la marée               //
        //    WaterElevation12  float qui contient 1/12 de l'élévation totale de la marée       //
        //    coefficients      liste contenant les différent coefficient cumulé de la marée    //
        //    i                 int qui nous donne entre quels coefficients se situe l'heure    //
        // FONCTIONS APPELEES :                                                                 //
        //                                                                                      //
        //     Minute                                                                           //
        // ALGO - REFERENCES :                                                                  //
        //                                                                                      //
        //----------------- FIN EN TETE --------------------------------------------------------//"""

    try:
        MinHour, MaxHour, MinLevel, MaxLevel = Minute(MinHour), Minute(MaxHour), float(MinLevel), float(MaxLevel)  # on mets les variables au bon format
        Var = Minute(Var)  # on récupère l'heure désirée
    except ValueError:  # si il y a une erreur avec une des variables
        print("""
Une des entrée de la fonction TideTime a mal été rentrée:
-MineHour:tupple contenant 2 int ex:MineHour=(11, 57) pour 11h57
-MaxHour:tupple contenant 2 int ex:MaxHour=(11, 57) pour 11h57
-MinLevel:float ex:MinLevel=3.45 pour 3,45m
-MaxLevel:float ex:MaxLevel=3.45 pour 3,45m
-Var:float ex:Var=3.45 pour 3,45m""")

    # print(MinHour, MaxHour, MinLevel, MaxLevel, Var)

    TideHour = MaxHour-MinHour  # variables qui contient la durée totale de la marée
    if TideHour < 0:  # si elle se passe sur 2 jours on traite les variables pour éviter une erreure de calcul
        MaxHour += 24*60  # on leur rajoute 24h en minute
        if Var < MinHour:  # au cas ou l'heure qu'on recherche est sur le deuxiéme jour
            Var += 24*60
        TideHour = MaxHour-MinHour  # on recalcule la durée totale de la marée pour avoir un résultat positif
    TideHour6 = TideHour/6  # on récupère sa valeur pour chaque graduations

    WaterElevation = float(MaxLevel - MinLevel)  # variable qui contient l'élévation totale de la marée
    WaterElevation12 = WaterElevation/12  # on récupère sa valeur pour chaque graduations

    coefficients = [0, 1, 3, 6, 9, 11, 12]  # les différents coefficients relatifs à la courbe de montée de la marée

    i = 0
    for i in range(7):
        if MinHour+i*TideHour6 >= Var:  # on recherche entre lesquels des 6 periodes se situe l'horaire recherché
            break

    # pour le détail des données utilisées dans les calculs:
    """print(str(MinHour+(i-1)*TideHour6).ljust(6), str(Var).ljust(6), str(MinHour+i*TideHour6).ljust(6))
    print(str(MinLevel + coefficients[i-1]*WaterElevation12).ljust(6), "?".ljust(6), str(MinLevel + coefficients[i]*WaterElevation12).ljust(6))"""

    # On retourne le résultat (niveau minimum + niveau pour atteindre la zone dans laquelle est l'heure + calcul avec un coefficient pour avoir la hauteur depuis la zone)
    return MinLevel + coefficients[i-1]*WaterElevation12 + (Var-MinHour-(i-1)*TideHour6)/TideHour6*(coefficients[i]-coefficients[i-1])*WaterElevation12


def TideTime(MinHour, MaxHour, MinLevel, MaxLevel, Var):
    """
        // ---------------- DEBUT EN TETE ------------------------------------------------------//
        // NOM :                    TideTime                                                    //
        //                                                                                      //
        // AUTEURS : JB Moufle                                                                  //
        //                                                                                      //
        // VERSION :    1.0         JB Moufle               28/09/2020                          //
        //     Calcule l'heure de la marée pour n'importe quel niveau                           //
        // HISTORIQUE : Aucun                                                                   //
        //                                                                                      //
        // ENTREES :  				                                                            //
        //	MinHour 		tuple de la forme (HH,MM) de l'heure de début de marée            	//
        //	MaxHour 		tuple de la forme (HH,MM) de l'heure de fin de marée                //
        //  MinLevel        float du niveau d'eau au début de la marée                          //
        //  MaxLevel        float du niveau d'eau a la fin de la marée                          //
        //	Var		        float du niveau d'eau que l'on recherche                            //
        //                                                                                      //
        // SORTIES :                                                                            //
        //	tuple de la forme (HH,MM) de l'heure recherché             	                        //
        // MODIFIEES :                                                                          //
        //                                                                                      //
        // LOCALES :                                                                            //
        //    MinHour 		    int de l'heure de début de marée en minute           	        //
        //	  MaxHour 		    int de l'heure de fin de marée en minute                        //
        //    MinLevel          float du niveau d'eau au début de la marée                      //
        //    MaxLevel          float du niveau d'eau a la fin de la marée                      //
        //	  Var		        float du niveau d'eau dont on recherche l'heure                 //
        //    TideHour          int correspondant à la durée en minute de l'heure marée         //
        //    TideHour6         float correspondant à la durée en minute d'1/12 de l'heure marée//
        //    WaterElevation    float qui contient l'élévation totale de la marée               //
        //    WaterElevation12  float qui contient 1/12 de l'élévation totale de la marée       //
        //    coefficients      liste contenant les différent coefficient cumulé de la marée    //
        //    i                 int qui nous donne entre quelles zones se situe le niveau d'eau //
        // FONCTIONS APPELEES :                                                                 //
        //                                                                                      //
        // ALGO - REFERENCES :                                                                  //
        //                                                                                      //
        //----------------- FIN EN TETE --------------------------------------------------------//"""

    try:
        MinHour, MaxHour, MinLevel, MaxLevel = Minute(MinHour), Minute(MaxHour), float(MinLevel), float(MaxLevel)
        Var = float(Var)
    except ValueError:
        print("""
Une des entrée de la fonction TideTime a mal été rentrée:
-MineHour:tupple contenant 2 int ex:MineHour=(11, 57) pour 11h57
-MaxHour:tupple contenant 2 int ex:MaxHour=(11, 57) pour 11h57
-MinLevel:float ex:MinLevel=3.45 pour 3,45m
-MaxLevel:float ex:MaxLevel=3.45 pour 3,45m
-Var:float ex:Var=3.45 pour 3,45m""")

    # print(MinHour, MaxHour, MinLevel, MaxLevel, Var)

    TideHour = MaxHour - MinHour  # variables qui contient la durée totale de la marée
    if TideHour < 0:  # si elle se passe sur 2 jours on traite les variables pour éviter une erreure de calcul
        MaxHour += 24 * 60  # on rajoute à l'heure max 24h en minute
        TideHour = MaxHour - MinHour  # on recalcule la durée totale de la marée pour avoir un résultat positif
    TideHour6 = TideHour / 6  # on récupère sa valeur pour chaque graduations

    WaterElevation = float(MaxLevel - MinLevel)  # variable qui contient l'élévation totale de la marée
    WaterElevation12 = WaterElevation / 12  # on récupère sa valeur pour chaque graduations

    coefficients = [0, 1, 3, 6, 9, 11, 12]  # les différents coefficients relatifs à la courbe de montée de la marée

    i = 0
    if WaterElevation >= 0:  # si l'élévation est positive
        for i in range(len(coefficients)):
            if MinLevel + coefficients[i]*WaterElevation12 >= Var:  # on recherche entre lesquels des periodes se situe l'élevation
                break
    else:  # si l'élévation est négative on fait la même chose mais avec les signes inversés
        for i in range(len(coefficients)):
            if MinLevel + coefficients[i]*WaterElevation12 <= Var:  # on recherche entre lesquels des periodes se situe l'élevation
                break

    # pour le détail des données utilisées dans les calculs:
    """print(str(MinHour + (i - 1) * TideHour6).ljust(6), "?".ljust(6), str(MinHour + i * TideHour6).ljust(6))
    print(str(MinLevel + coefficients[i - 1] * WaterElevation12).ljust(6), str(Var).ljust(6), str(MinLevel + coefficients[i] * WaterElevation12).ljust(6))"""

    # On calcul le résultat ( calcul avec un coefficient pour avoir l'heure à partir d'un niveau)
    Hour = int(((Var-(MinLevel + coefficients[i - 1] * WaterElevation12)) / ((coefficients[i] - coefficients[i - 1]) * WaterElevation12) * TideHour6 + MinHour + (i - 1) * TideHour6).__round__())

    # si l'heure se passe sur un autre jour
    if int(Hour/60) >= 24:
        Hour -= 24*60

    # on retourne l'heure sous la forme d'une tuple heure, minute
    return int(Hour/60), int(Hour-60*int(Hour/60))


def Minute(var):
    """
        // ---------------- DEBUT EN TETE ------------------------------------------------------//
        // NOM :                    Minute                                                      //
        //                                                                                      //
        // AUTEURS : JB Moufle                                                                  //
        //                                                                                      //
        // VERSION :    1.0         JB Moufle               28/09/2020                          //
        //     Permet de convertir une tuple horaire (HH,MM) en minutes                         //
        // HISTORIQUE : Aucun                                                                   //
        //                                                                                      //
        // ENTREES :  				                                                            //
        //	var             la tuple sous la forme (HH,MM)                                      //
        //                                                                                      //
        // SORTIES :                                                                            //
        //	var             int correspondant au nombre de minute de la tuple                   //
        // MODIFIEES :                                                                          //
        //                                                                                      //
        // LOCALES :                                                                            //
        //	  var               la tuple sous la forme (HH,MM)                                  //
        //                                                                                      //
        // FONCTIONS APPELEES :                                                                 //
        //                                                                                      //
        // ALGO - REFERENCES :                                                                  //
        //                                                                                      //
        //----------------- FIN EN TETE --------------------------------------------------------//"""
    h, m = int(var[0]), int(var[1])
    return int(h * 60 + m)


"""quelques exemples:
print(TideLevel((00, 30), (6, 30), 1, 13, (4, 30)))
print(TideTime((00, 30), (6, 30), 13, 1, 11))"""