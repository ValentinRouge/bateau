from cascade_resultats import CCtoCV


cc = int(input("donnez la  valuer du cap compas : "))
d = int(input("donnez la  valuer de la déviation : "))
a = int(input("donnez la  valuer du choix de la direction (1 - Est 2 - West) : "))
D = int(input("donnez la  valuer de la déclinaison : ")) 
b = int(input("donnez la  valuer du choix de la direction (1 - Est 2 - West) : "))  
print ("\nle cap vrai est :", CCtoCV(cc,d,a,D,b))
