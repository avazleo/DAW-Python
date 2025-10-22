alumnos = int(input("Introduce el número de alumnos: "))
materias = int(input("Introduce el número de materias: "))

matriz_resultado = [[0 for _ in range(materias)] for _ in range(alumnos)]

medias = []
medias_asignaturas = [0 for _ in range(materias)]

for i in range(alumnos):
    count = 0
    for j in range(materias):
        nota = int(input(f"Introduce la nota del alumno {i} para la materia {j}: "))
        matriz_resultado[i][j] = nota
        count += nota
        medias_asignaturas[j] += nota
    medias.append(count/materias)

for j in range(materias):
    medias_asignaturas[j] = medias_asignaturas[j]/alumnos

print(medias)
print(medias_asignaturas)


