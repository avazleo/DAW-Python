# Suma de matrices. Pide al usuario dos matrices 2x2 y calcula su suma elemento a elemento.

ROWS = 2
COLUMNS = 2
matriz_1 = []
matriz_2 = []

# Bucle para introducir los valores en las 2 matrices
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un numero para la matriz_1 [{i},{j}]: "))
        fila.append(num)
    matriz_1.append(fila)

for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un numero para la matriz_2 [{i},{j}]: "))
        fila.append(num)
    matriz_2.append(fila)

# Bucle para sumar las dos matrices introducidas
matriz_suma = []
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num_sum = matriz_1[i][j] + matriz_2[i][j]
        fila.append(num_sum)
    matriz_suma.append(fila)

# Muestro la matriz 1, 2 y su suma
print("La Matriz 1 es: ")
for fila in matriz_1:
    print(fila)

print("La Matriz 2 es: ")
for fila in matriz_2:
    print(fila)

print("La Matriz suma es: ")
for fila in matriz_suma:
    print(fila)