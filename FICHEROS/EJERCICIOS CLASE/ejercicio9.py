fichero = input("Ingrese el nombre del fichero: ")
try:
    with open(fichero, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("El fichero no existe")
except PermissionError:
    print("No tienes permisos para leer el fichero")
finally:
    print("Programa finalizado")