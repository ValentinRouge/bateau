from maree import *
"""permet de faire des tests sur le fichier maree.py, il faut l'executer pour voir les résultats"""

print("       | calcul |   | theory |compare|")

# exemple 1: (pris sur le site https://www.navigation-accompagnee.fr/fiche-detail/5b7c252a7d560d0008e1e17c)
# test 1
print("test1: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (13, 47)).__round__(2)).rjust(8), "<=> 0.70    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (13, 47)).__round__(2) == float(0.70))

# test 2
print("test2: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (14, 44)).__round__(2)).rjust(8), "<=> 1.13    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (14, 44)).__round__(2) == float(1.13))

# test 3
print("test3: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (15, 41)).__round__(2)).rjust(8), "<=> 2.00    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (15, 41)).__round__(2) == float(2.00))

# test 4
print("test4: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (16, 38)).__round__(2)).rjust(8), "<=> 3.30    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (16, 38)).__round__(2) == float(3.30))

# test 5
print("test5: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (17, 35)).__round__(2)).rjust(8), "<=> 4.60    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (17, 35)).__round__(2) == float(4.60))

# test 6
print("test6: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (18, 32)).__round__(2)).rjust(8), "<=> 5.47    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (18, 32)).__round__(2) == float(5.47))

# test 7
print("test7: ", str(TideLevel((13, 47), (19, 30), 0.7, 5.93, (19, 29)).__round__(2)).rjust(8), "<=> 5.90    ", TideLevel((13, 47), (19, 30), 0.7, 5.93, (19, 29)).__round__(2) == float(5.90))

# test 8
print("test8: ", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 0.7)).rjust(8), "<=> (13, 47)", TideTime((13, 47), (19, 30), 0.7, 5.93, 0.7) == (13, 47))

# test 9
print("test9: ", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 1.13)).rjust(8), "<=> (14, 44)", TideTime((13, 47), (19, 30), 0.7, 5.93, 1.13) == (14, 44))

# test 10
print("test10:", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 2.00)).rjust(8), "<=> (15, 41)", TideTime((13, 47), (19, 30), 0.7, 5.93, 2.00) == (15, 41))

# test 11
print("test11:", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 3.30)).rjust(8), "<=> (16, 38)", TideTime((13, 47), (19, 30), 0.7, 5.93, 3.30) == (16, 38))

# test 12
print("test12:", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 4.60)).rjust(8), "<=> (17, 35)", TideTime((13, 47), (19, 30), 0.7, 5.93, 4.60) == (17, 35))

# test 13
print("test13:", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 5.47)).rjust(8), "<=> (18, 32)", TideTime((13, 47), (19, 30), 0.7, 5.93, 5.47) == (18, 32))

# test 14
print("test14:", str(TideTime((13, 47), (19, 30), 0.7, 5.93, 5.90)).rjust(8), "<=> (19, 29)", TideTime((13, 47), (19, 30), 0.7, 5.93, 5.90) == (19, 29))


# exemple 2: (avec un décalage de jour. résultats calculés)
# test 15
print("test15:", str(TideLevel((23, 00), (5, 00), 1.5, 13.5, (2, 00))).rjust(8), "<=> 7.50    ", TideLevel((23, 00), (5, 00), 1.5, 13.5, (2, 00)) == 7.50)

# test 16
print("test16:", str(TideLevel((23, 00), (5, 00), 1.5, 13.5, (23, 30))).rjust(8), "<=> 2.00    ", TideLevel((23, 00), (5, 00), 1.5, 13.5, (23, 30)) == 2.00)

# test 17
print("test18:", str(TideTime((23, 00), (5, 00), 1.5, 13.5, 7.5)).rjust(8), "<=> (2, 0)  ", TideTime((23, 00), (5, 00), 1.5, 13.5, 7.5) == (2, 0))

# test 19
print("test19:", str(TideTime((23, 00), (5, 00), 1.5, 13.5, 2.00)).rjust(8), "<=> (23, 30)", TideTime((23, 00), (5, 00), 1.5, 13.5, 2.00) == (23, 30))


# exemple 3: (avec une marée descendante. résutats calculés)
# test 20
print("test20:", str(TideLevel((23, 00), (5, 00), 13.5, 1.5, (2, 00))).rjust(8), "<=> 7.50    ", TideLevel((23, 00), (5, 00), 13.5, 1.5, (2, 00)) == 7.50)
