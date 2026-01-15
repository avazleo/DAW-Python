try:
    numero = int(input("Introduce un número entero: "))
    print("El doble es:", numero * 2)
except ValueError:
    print("Error: debes introducir un número entero")