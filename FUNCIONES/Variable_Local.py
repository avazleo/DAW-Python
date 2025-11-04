# Defino la función suma_local que recibe dos variables como parámetros y la suma
def suma_local(a, b):
    suma = a + b
    print(suma)

# Main
a = int(input("Introduce un numero: "))
b = int(input("Introduce un numero: "))

suma = 0
suma_local(a, b)

print(suma)