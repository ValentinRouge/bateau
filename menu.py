while True:
    print("""
0\Quitter
1\Calcul de position
2\Calcul de cap
3\Calcul de maree
""")
    answ = input("Que souhaitez vous faire?\n:")
    try:
        answ = int(answ)
    except ValueError:
        print("impossible de rentrer autre chose que des chiffres (O, 1, 2 ,3)  en fonction de ce que l'on souhaite réaliser")

    if answ == 0:
        break
    elif answ == 1:
        print("Calcul de position")
    elif answ == 2:
        print("Calcul de cap")
    elif answ == 3:
        print("Calcul de maree")