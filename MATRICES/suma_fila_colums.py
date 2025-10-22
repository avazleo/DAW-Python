# Suma de filas y columnas. Dada una matriz de 3x3, calcula y muestra la suma de cada fila y cada columna.

ROWS = 3
COLUMNS = 3
matriz = []

# Bucle para introducir los elementos de la matriz
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un elemento [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Muestro la matriz para comprobar que la suma es correcta
for fila in matriz:
    print(fila)

# Bucle para sumar los datos de cada fila
for i in range(ROWS):
    sum_row = 0
    for j in range(COLUMNS):
        sum_row += matriz[i][j]
    print(f"La suma de la fila {i} es: {sum_row}")

# Bucle para sumar los datos de cada columna
for j in range(COLUMNS):
    sum_column = 0
    for i in range(ROWS):
        sum_column += matriz[i][j]
    print(f"La suma de la columna {j} es: {sum_column}")

