f = open("nombres.txt", "rt")
contador = 0
linea = f.readline()
while linea != "":
    contador +=1
    print(linea.rstrip())
    linea = f.readline()
f.close()
print(f"El numero de nombres es: {contador}")

contador = 0
with open("nombres.txt", "r") as f:
    for _ in f:
        contador += 1
    print("Total de nombres:", contador)