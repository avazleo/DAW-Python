try:
    with open("datos.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe")
