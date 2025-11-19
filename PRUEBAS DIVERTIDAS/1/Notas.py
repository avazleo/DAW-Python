# Programa que calcula la media de notas y muestra diferencias respecto a ella

# Creamos una lista vacía para guardar las notas
notas = []

# Pedimos las notas de 5 alumnos
for i in range(5):
    nota = float(input(f"Introduce la nota del alumno {i+1}: "))
    notas.append(nota)

# Calculamos la media
media = sum(notas) / len(notas)

print("\nNotas introducidas:", notas)
print("Media del grupo:", media)

# Mostramos qué notas están por encima y por debajo de la media
print("\nResultados:")

for i in range(5):
    diferencia = notas[i] - media
    if notas[i] > media:
        print(f"El alumno {i+1} tiene {notas[i]} (por ENCIMA de la media, +{diferencia:.2f})")
    elif notas[i] < media:
        print(f"El alumno {i+1} tiene {notas[i]} (por DEBAJO de la media, {diferencia:.2f})")
    else:
        print(f"El alumno {i+1} tiene {notas[i]} (IGUAL a la media)")