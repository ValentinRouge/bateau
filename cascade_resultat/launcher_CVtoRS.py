from cascade_resultats import CVtoRS


cv = int(input("donnez la  valuer du cap vrai : "))
a = int(input("donnez la  valuer de la valeur de la derive : "))             
print("\nla route de surface est :", CVtoRS(cv,a))
