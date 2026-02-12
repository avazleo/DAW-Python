import csv

filas = [
    ("nombre", "edad", "curso"),
    ("Ana", "19", "DAW1"),
    ("Luis", "17", "DAW1"),
    ("María", "20", "DAW1"),
]
with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(filas)