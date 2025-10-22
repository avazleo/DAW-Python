# Multiplicación de matrices: Implementa el producto de dos matrices cuadradas de 2x2 o 3x3.

matriz_1 = []
matriz_2 = []

n = int(input("Introduce el valor n para crear una matriz n x n: "))
ROWS = n
COLUMNS = n

# Bucle para introducir los elementos de las dos matrices
print("Matriz 1")
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un elemento [{i},{j}]: "))
        fila.append(num)
    matriz_1.append(fila)

print("Matriz 2")
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un elemento [{i},{j}]: "))
        fila.append(num)
    matriz_2.append(fila)

# Bucle para multiplicar matrices
matriz_3 = []
for i in range(n):
    fila = []
    for j in range(n):
        suma = 0
        for k in range(n):
            suma += matriz_1[i][k] * matriz_2[k][j]
        fila.append(suma)
    matriz_3.append(fila)

print("Matriz 1")
for i in range(ROWS):
    for j in range(COLUMNS): print(matriz_1[i][j], end=" ")
    print()

print("Matriz 2")
for i in range(ROWS):
    for j in range(COLUMNS): print(matriz_2[i][j], end=" ")
    print()

print("Multuplicación")
for i in range(ROWS):
    for j in range(COLUMNS): print(matriz_3[i][j], end=" ")
    print()
