from maree import Minute
"""diferents test de la fonction Minute"""

print("       |entree|sortie|attendu|compare|")

# test1
H = (2, 30)
print("test1:", str(H).rjust(8), str(Minute(H)).rjust(4), str(150).rjust(7), "  ", str(Minute(H) == 150))
# test2
H = (0, 45)
print("test2:", str(H).rjust(8), str(Minute(H)).rjust(4), str(45).rjust(7), "  ", str(Minute(H) == 45))
# test3
H = (23, 00)
print("test3:", str(H).rjust(8), str(Minute(H)).rjust(4), str(1380).rjust(7), "  ", str(Minute(H) == 1380))
# test4
H = (12, 22)
print("test4:", str(H).rjust(8), str(Minute(H)).rjust(4), str(742).rjust(7), "  ", str(Minute(H) == 742))
