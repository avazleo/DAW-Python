import csv
from collections import Counter

total_validas = 0
suma_edades = 0
cursos = Counter()

with open("alumnos.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    for row in reader:
        try:
            edad = int(row["edad"])
        except ValueError:
            continue
        total_validas += 1
        suma_edades += edad
        cursos[row["curso"]] += 1

if total_validas == 0:
    print("No hay filas válidas")
else:
    media = suma_edades / total_validas
    curso_mas_frecuente = cursos.most_common(1)[0][0]
    print("Filas válidas:", total_validas)
    print("Edad media:", media)
    print("Curso más frecuente:", curso_mas_frecuente)
