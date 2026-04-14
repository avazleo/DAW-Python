import csv
import json
alumnos = []
with open("alumnos.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        try:
            row["edad"] = int(row["edad"])
        except ValueError:
            print("El numero no es valido")
            continue
        alumnos.append(row)

with open("alumnos.json", "w", encoding="utf-8") as f:
    json.dump(alumnos, f, ensure_ascii=False, indent=4)
