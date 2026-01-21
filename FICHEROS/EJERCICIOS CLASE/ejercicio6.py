f = open("lenguajes.txt", "rt")
lenguajes = f.readlines()
print(lenguajes)
f.close()

with open("lenguajes.txt", "rt") as f:
    lenguajes = f.readlines()
    print(lenguajes)

lenguajes = []
with open("lenguajes.txt", "rt") as f:
    for linea in f:
        lenguajes.append(linea.strip())
    print(lenguajes)