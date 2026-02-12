with open("alumnos.csv", "r", encoding="utf-8") as f:
    lineas = f.read().splitlines()

# Ojo: la primera línea es la cabecera
for linea in lineas[1:]:
    nombre, edad, curso = linea.split(",")
    print(f"Nombre: {nombre} | Edad: {edad} | Curso: {curso}")