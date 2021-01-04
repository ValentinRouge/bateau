from maree import *

def HourToTupples(Hour):
    """
        // ---------------- DEBUT EN TETE ------------------------------------------------------//
        // NOM :                    HourToTupples                                               //
        //                                                                                      //
        // AUTEURS : JB Moufle                                                                  //
        //                                                                                      //
        // VERSION :    1.0         JB Moufle               28/09/2020                          //
        //     Permet de convertir un string horaire HH:MM en tupple horaire (HH,MM)            //
        // HISTORIQUE : Aucun                                                                   //
        //                                                                                      //
        // ENTREES :  				                                                            //
        //	Hour            string de la forme HH:MM                                            //
        //                                                                                      //
        // SORTIES :                                                                            //
        //	h               int correspondant à HH du string                                    //
        //  m               int correspondanat à MM du string                                   //
        //                                                                                      //
        // MODIFIEES :                                                                          //
        //                                                                                      //
        // LOCALES :                                                                            //
        //	    h               int correspondant à HH du string                                //
        //      m               int correspondanat à MM du string                               //
        //                                                                                      //
        // FONCTIONS APPELEES :                                                                 //
        //                                                                                      //
        // ALGO - REFERENCES :                                                                  //
        //                                                                                      //
        //----------------- FIN EN TETE --------------------------------------------------------//"""
    h, m = Hour.split(":")
    return int(h), int(m)

def launch_marre():
    """
    // ---------------- DEBUT EN TETE ------------------------------------------------------//
    // NOM :                    HourToTupples                                               //
    //                                                                                      //
    // AUTEURS : JB Moufle & V Rouge                                                        //
    //                                                                                      //
    // VERSION :    1.0                                 04/01/2021                          //
    //     lance le programme marée                                                         //
    // HISTORIQUE : Aucun                                                                   //
    //                                                                                      //
    // ENTREES :  				                                                            //
    //                                                                                      //
    // SORTIES :                                                                            //
    //                                                                                      //
    // MODIFIEES :                                                                          //
    //                                                                                      //
    //                                                                                      //
    // FONCTIONS APPELEES :                                                                 //
    //             hourtotuple, tide level, tidetime                                        //
    // ALGO - REFERENCES :                                                                  //
    //                                                                                      //
    //----------------- FIN EN TETE --------------------------------------------------------//"""
    while True:
        choice = str(input("""
        Menu:
        1-Rechercher le niveau de la marée grace à un horaire
        2-Rechercher l'heure à laquelle la marée atteint un certain niveau
        3-Quitter
        :""")).strip()  # on demande à l'utilisateur de rentrer un des choix
        print("")  # juste pour le saut de ligne

        if choice == "1":  # si le choix est 1
            try:
                MinHour = HourToTupples(input("Premiére Heure:  "))
                MinLevel = float(input("Niveau correspondant à la premiére heure:  "))
                MaxHour = HourToTupples(input("Deuxième heure:  "))
                MaxLevel = float(input("Niveau correspondant à la deuxième heure:  "))
                Var = HourToTupples(input("Heure désirée:   "))
                Solution = maree.TideLevel(MinHour, MaxHour, MinLevel, MaxLevel, Var)
                print("\nà {}h{} la mer sera à {}m\n\n".format(str(Var[0]).rjust(2, "0"), str(Var[1]).rjust(2, "0"), Solution.__round__(2)))
            except ValueError:
                print("""
                Une des entrées n'est pas correcte:
                -pour les heure il faut rentrer l'heure sous la forme hh:mm   ex: "11:57"
                -Pour les niveau d'eau il faut rentrer un nombre avec un point pour les décimales   ex: "3.28"
                """)
        elif choice == "2":  # sinon si le choix et 2
            try:
                MinHour = HourToTupples(input("Premiére Heure:  "))
                MinLevel = float(input("Niveau correspondant à la premiére heure:  "))
                MaxHour = HourToTupples(input("Deuxième heure:  "))
                MaxLevel = float(input("Niveau correspondant à la deuxième heure:  "))
                Var = float(input("Niveau d'on on souhaite connaître l'heure: "))
                Solution = maree.TideTime(MinHour, MaxHour, MinLevel, MaxLevel, Var)
                print("la mer atteindra {}m à {}h{}".format(Var, str(Solution[0]).rjust(2, "0"), str(Solution[1]).rjust(2, "0")))
            except ValueError:
                print("""
        Une des entrées n'est pas correcte:
        -pour les heure il faut rentrer l'heure sous la forme hh:mm   ex: "11:57"
        -Pour les niveau d'eau il faut rentrer un nombre avec un point pour les décimales   ex: "3.28"
        """)
        elif choix == "3":  # sinon si le choix est 3
            break   # on arrete la fonction
        else:  # sinon pour toutes les autres réponses (incompréhension de l'utilisateur)
            print("\nil faut rentrer un nombre en fonction de ce que l'on souhaite réaliser.\n1, 2 ou 3 (pour quitter)\n")


