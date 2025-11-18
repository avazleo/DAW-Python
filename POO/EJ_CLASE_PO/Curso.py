class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre


class Curso():
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def listar_alumnos(self):
        return self.alumnos

def main():
    curso = Curso("1DAW-B")
    al1 = Alumno("Jose Carlos")
    al2 = Alumno("Naira")

    curso.agregar_alumno(al1)
    curso.agregar_alumno(al2)

    alumnos = curso.listar_alumnos()

    for alumno in alumnos:
        print(f"El nombre del alumno es: {alumno.nombre}")

if __name__ == "__main__":
    main()
