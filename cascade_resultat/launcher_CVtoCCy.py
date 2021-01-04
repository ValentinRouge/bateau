from cascade_resultats import CVtoCC


cv = int(input("donnez la  valuer du cap vrai : "))
d = int(input("donnez la  valuer de la déviation : "))
a = int(input("donnez la  valuer du choix de la direction (1 - Est 2 - West) : "))
D = int(input("donnez la  valuer de la déclinaison : ")) 
b = int(input("donnez la  valuer du choix de la direction (1 - Est 2 - West) : "))              
print("\nle cap compas est :", CVtoCC(cv,d,a,D,b))
