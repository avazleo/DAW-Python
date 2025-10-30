# Programa que crea una matriz NxN y suma una fila indicada por el usuario

# Pedimos el tamaño de la matriz
n = int(input("Introduce el tamaño N de la matriz (NxN): "))

# Creamos la matriz vacía
matriz = []

# Rellenamos la matriz con números introducidos por el usuario
print("Introduce los valores de la matriz:")
for i in range(n):
    fila = []
    for j in range(n):
        num = int(input(f"Elemento [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Mostramos la matriz completa
print("\nMatriz introducida:")
for fila in matriz:
    print(fila)

# Pedimos al usuario qué fila quiere sumar
while True:
    fila_sumar = int(input(f"\n¿Qué fila deseas sumar? (0 a {n-1}): "))
    if fila_sumar >= 0 and fila_sumar <= n:
        break
    else:
        print("El número de fila introducido no es correcto.")

# Calculamos la suma de la fila elegida
suma = 0
for j in range(n):
    suma += matriz[fila_sumar][j]

suma = sum(matriz[fila_sumar])



print(f"La suma de los elementos de la fila {fila_sumar} es: {suma}")