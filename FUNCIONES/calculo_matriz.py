def calculo_matriz(matriz, operacion, numero):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(n):
        for j in range(m):
            match operacion:
                case "+":
                    matriz[i][j] += numero
                case "-":
                    matriz[i][j] -= numero
                case "*":
                    matriz[i][j] *= numero
                case "/":
                    matriz[i][j] /= numero

def main():
    matriz = [[0 for _ in range(3)] for _ in range(3)]
    calculo_matriz(matriz, "+", 2)
    print(matriz)
    calculo_matriz(matriz, "+", 2)
    print(matriz)

if __name__ == "__main__":
    main()

