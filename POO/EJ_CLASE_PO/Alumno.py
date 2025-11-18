class Alumno:
    def __init__(self, nota):
        if nota > 0 and nota <= 10:
            self.__nota = float(nota)
        else:
            print("⚠️ Nota invalida. Nota por defecto: 0")

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = float(nota)
        else:
            raise ValueError("Nota inválida. Debe estar entre 0 y 10.")

def main():
    alu1 = Alumno(10)
    print(f"La nota del alumno es {alu1.nota:.2f}")
    alu1.nota = 8
    print(f"La nota del alumno es {alu1.nota:.2f}")

    alu2 = Alumno(7)
    try:
        alu2.nota = -2
        print("✅ Calificación modificada con éxito")
    except ValueError:
        print("⚠️ Error: nota inválida.")

    alu2.nota = 9
    print(f"La nota del alumno es {alu2.nota:.2f}")

    try:
        alu2.nota = 11
        print("✅ Calificación modificada con éxito")
    except ValueError:
        print("⚠️ Error: nota inválida.")


if __name__ == "__main__":
    main()