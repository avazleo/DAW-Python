# Generar y mostrar matriz: Crea una matriz de 3x3 con números enteros introducidos por el usuario.
# Muestra la matriz en formato cuadrado

ROWS = 3
COLUMNS = 3
matriz = []

for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = int(input(f"Introduce un elemento [{i},{j}]: "))
        fila.append(num)
    matriz.append(fila)

# Imprimimos la Matriz en formato cuadrado de tres formas dificiles

for i in range(ROWS):
    print(f"{matriz[i][0]} {matriz[i][1]} {matriz[i][2]}")

for fila in matriz:
    print(fila)

for i in range(ROWS):
    for j in range(COLUMNS): print(matriz[i][j], end=" ")
    print()

