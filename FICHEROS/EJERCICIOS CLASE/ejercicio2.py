f = open("mensaje.txt", "rt")
mensaje = f.read()
print(mensaje)
f.close()

with open("mensaje.txt", "r") as f:
    print(f.read())