nota = float(input("Ingresa una nota: "))

if nota <5:
    print("Suspenso")
else:
    if nota >= 5 and nota < 6:
        print ("Aprobado")
    elif nota >= 6 and nota < 7:
        print ("Bien")
    elif nota >= 7 and nota < 9:
        print("Notable")
    else:
        print("Sobresaliente")

