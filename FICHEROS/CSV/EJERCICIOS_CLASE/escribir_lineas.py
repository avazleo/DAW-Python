filas = [
    ("nombre", "edad", "curso"),
    ("Ana", "19", "DAW1"),
    ("Luis", "17", "DAW1"),
    ("María", "20", "DAW1"),
    ]
with open("alumnos.csv", "w", encoding="utf-8") as f:
    for fila in filas:
        f.write(",".join(fila) + "\n")