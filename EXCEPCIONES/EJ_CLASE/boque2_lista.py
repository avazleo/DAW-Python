nombres = ["Ana", "Luis", "María", "Carlos"]
try:
    posicion = int(input("Introduce una posición: "))
    print(nombres[posicion])
except IndexError:
    print("Error: posición fuera de rango")
except ValueError:
    print("Error: debes introducir un número")