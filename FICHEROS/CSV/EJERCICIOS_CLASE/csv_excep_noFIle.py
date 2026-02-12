import csv

nombre_fichero = input("Nombre del CSV: ")
try:
    with open(nombre_fichero, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for fila in reader:
            print(fila)
except FileNotFoundError:
    print("Error: el fichero no existe")
except PermissionError:
    print("Error: no tienes permisos para leer el fichero")