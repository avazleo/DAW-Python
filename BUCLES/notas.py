# Gestor simple de notas de un alumno
# Permitir introducir varias notas (usando un bucle).
# Calcular la media.
# Determinar si el alumno/a aprueba o suspende (condicional).
# Mostrar el resultado con un mensaje claro.

notes_numbers = 0
notes_sum = 0

while True:
    note = float(input("Introduce la calificación (número negativo para dejar de introducir notas): "))
    if note < 0:
        break
    elif note > 10:
        print(f"La calificación introducida no es correcta, debe ser entre 0 y 10.\nPruebe otra vez")
    else:
        notes_numbers += 1
        notes_sum += note

media = notes_sum / notes_numbers
if media < 5:
    print(f"El alumno/a suspende con una media de: {media:.2f}")
else:
    print(f"El alumno/a aprueba con una media de: {media:.2f}")

