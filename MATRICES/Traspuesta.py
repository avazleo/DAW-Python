# Matriz traspuesta: Escribe un programa que calcula la matriz traspuesta (filas por columnas).

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

# Bucles para crear la matriz traspuesta
m_traspuesta = []
for j in range(COLUMNS):
    fila = []
    for i in range(ROWS):
        fila.append(matriz[i][j])
    m_traspuesta.append(fila)

# Muestro la matriz original y la traspuesta

print("Matriz original")
for fila in matriz:
    print(fila)

print("Matriz traspuesta")
for fila in m_traspuesta:
    print(fila)