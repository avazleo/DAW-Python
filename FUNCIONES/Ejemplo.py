# Función para crear matrices
def crear_matriz(ROWS, COLUMNS):
    matriz = []
    for i in range(ROWS):
        fila = []
        for j in range(COLUMNS):
            num = int(input(f"Enter the matrix [{i},{j}]: "))
            fila.append(num)
        matriz.append(fila)
    return matriz

# Función para mostrar matrices
def mostrar_matriz(matriz, ROWS, COLUMNS):
    for i in range(ROWS):
        for j in range(COLUMNS): print(matriz[i][j], end=" ")
        print()

# Main
ROWS = 2
COLUMNS = 2
matriz_1 = []
matriz_2 = []

print("Matriz 1:")
matriz_1 = crear_matriz(ROWS, COLUMNS)
print("Matriz 2:")
matriz_2 = crear_matriz(ROWS, COLUMNS)

# Bucle para sumar las dos matrices introducidas
matriz_suma = []
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num_sum = matriz_1[i][j] + matriz_2[i][j]
        fila.append(num_sum)
    matriz_suma.append(fila)

print("Matriz 1:")
mostrar_matriz(matriz_1, ROWS, COLUMNS)
print("Matriz 2:")
mostrar_matriz(matriz_2, ROWS, COLUMNS)
print("Matriz suma:")
mostrar_matriz(matriz_suma, ROWS, COLUMNS)
