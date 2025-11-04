def matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def main():
    matriz = matriz_identidad(3)
    print(matriz)

if __name__ == '__main__':
    main()
