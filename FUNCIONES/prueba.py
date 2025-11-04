import funciones_matrices as matriz

def main():
    n = int(input("Ingrese el numero de filas de la matriz: "))
    m = int(input("Ingrese el numero de columnas de la matriz: "))
    matriz_resultado = matriz.crear_matriz(n, m)
    matriz.mostrar_matriz(matriz_resultado)

if __name__ == "__main__":
    main()