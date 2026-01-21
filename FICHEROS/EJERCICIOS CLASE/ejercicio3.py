f = open("nombres.txt", "rt")
linea = f.readline()
while linea != "":
    print(linea.rstrip())
    linea = f.readline()
f.close()

with open("nombres.txt", "r") as f:
    for linea in f:
        print(linea.strip())
