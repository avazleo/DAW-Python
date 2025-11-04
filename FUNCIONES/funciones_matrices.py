def crear_matriz(filas, columnas):
    matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
    return matriz


def mostrar_matriz(matriz):
    ROWS = len(matriz)
    COLUMNS = len(matriz[0])
    for i in range(ROWS):
        for j in range(COLUMNS): print(matriz[i][j], end=" ")
        print()


def main():
    n = int(input("Ingrese el numero de filas de la matriz: "))
    m = int(input("Ingrese el numero de columnas de la matriz: "))
    matriz_resultado = crear_matriz(n, m)
    mostrar_matriz(matriz_resultado)


if __name__ == "__main__":
    main()
