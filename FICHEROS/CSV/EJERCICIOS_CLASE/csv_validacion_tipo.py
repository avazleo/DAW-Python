import csv

with open("alumnos.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        try:
            edad = int(row["edad"])
        except ValueError:
            print(f"Aviso: edad inválida en fila: {row}")
            continue
        print(row["nombre"], edad, row["curso"])