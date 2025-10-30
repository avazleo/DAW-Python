def matriz_identidad(n):
    matriz_resultado = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matriz_resultado[i][j] = 1
    return matriz_resultado

def main():
    n = int(input("Ingresa un numero N de una matriz NxN: "))
    matriz_resultado = matriz_identidad(n)
    print(matriz_resultado)

if __name__ == '__main__':
    main()