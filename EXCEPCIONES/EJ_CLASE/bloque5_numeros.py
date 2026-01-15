while True:
    try:
        numero = int(input("Introduce un número entero: "))
        break
    except ValueError:
        print("Entrada no válida, inténtalo de nuevo")

print("Número correcto:", numero)