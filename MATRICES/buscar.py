# Buscar en matriz. En una matriz 3x3 de palabras, busca una palabra y muestra su posición (fila y columna)

ROWS = 3
COLUMNS = 3
matriz = []

for i in range(ROWS):
    fila = []
    for j in range(COLUMNS):
        num = input(f"Introduce una palabra [{i},{j}]: ")
        fila.append(num)
    matriz.append(fila)

work = input("Introduce una palabra a buscar en la matriz: ")

find = False
for i in range(ROWS):
    if work in matriz[i]:
        find = True
        index = matriz[i].index(work)
        print(f"La palabra {work} existe en la lista en la posicion [{i}][{index}]")

if find == False:
    print(f"La palabra {work} no existe en la lista")