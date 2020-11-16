from coordonnee import convertLatLongXY

a=input("Latitude :")
b=input("Longitude :")

X,Y=convertLatLongXY(a,b)
print(X,Y)
