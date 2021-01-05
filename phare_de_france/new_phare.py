from json import *

def new_phare(lat, long):
    with open('phare_de_france\phare_de_France_dict.json') as json_data:  # on charge la liste des phare de france
        phare_de_france = load(json_data)
    sel = input("Voulez vous enregistrer dans la liste le phare que vous venez d'écrire ? \n1: Oui \n2: Non\n")
    if sel=="1":
        nom = input("Quel est le nom du phare ?")
        phare_de_france[nom]=[int(lat),int(long)]
        with open('phare_de_france\phare_de_France_dict.json', 'w') as json_data:
            json_data.write(dumps(phare_de_france)) #on réenregistre la liste des phares
        print("phare enregistré")
        print("-" * 40, sep="")  # affichage
    elif sel =="2":
        pass
    else:
        print("Veuillez entrer 1 ou 2")

    return phare_de_france
