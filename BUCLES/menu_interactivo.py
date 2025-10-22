#Crear un menú interactivo con opciones
# (ejemplo: 1. Calcular área de un circulo,
# 2. Calcular el área de un rectángulo, 3. Salir).
# El menú debe repetirse hasta que se elija salir.

#Importamos la funcion pi de math
from math import pi

#Ciclo para el menú
while True:
    print("MENU")
    print("=====")
    print(f"1. Calcular área de un circulo")
    print(f"2. Calcular área de un rectangulo")
    print(f"3. Salir")
    opc = int(input("Elige una opcion: "))
    if opc == 1:
        radio = float(input("Introduce el radio: "))
        print(f"El área de un circulo es: {pi*radio**2:.2f}")
    elif opc == 2:
        base = float(input("Introduce el base: "))
        altura = float(input("Introduce la altura: "))
        print(f"El area del rectangulo es: {base*altura:.2f}")
    elif opc == 3:
        break
    else:
        print("Opcion no valida")

print(f"Bye bye!")
