# Diagonal principal y secundaria. Dada una matriz n x n, muestra los elementos de la diagonal principal y secundaria.

matriz = []

n = int(input("Introduce el valor n para crear una matriz n x n: "))
ROWS = n
COLUMNS = n

# Bucle para introducir los elementos de la matriz
for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un elemento [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Bucle para mostrar los elementos de la diagonal principal
diagonal_principal = []
diagonal_secundaria = []
for i in range(ROWS):
    for j in range(COLUMNS):
        if j == i:
            diagonal_principal.append(matriz[i][j])
        if j+i == n-1:
            diagonal_secundaria.append(matriz[i][j])

# Muestro la matriz para comprobar que la suma es correcta
for fila in matriz:
    print(fila)

# Muestro la diagonal principal y la secundaria
print(f"La diagonal principal es {diagonal_principal}")
print(f"La diagonal secundaria es {diagonal_secundaria}")
