import sqlite3


class Alumno:
    def __init__(self, nombre, edad, id=None):
        self.id = id
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Alumno(id={self.id}, nombre='{self.nombre}', edad={self.edad})"


class Asignatura:
    def __init__(self, nombre, horas, id=None):
        self.id = id
        self.nombre = nombre
        self.horas = horas

    def __str__(self):
        return f"Asignatura(id={self.id}, nombre='{self.nombre}', horas={self.horas})"


class Matricula:
    def __init__(self, alumno_id, asignatura_id, nota, id=None):
        self.id = id
        self.alumno_id = alumno_id
        self.asignatura_id = asignatura_id
        self.nota = nota

    def __str__(self):
        return (
            f"Matricula(id={self.id}, alumno_id={self.alumno_id}, "
            f"asignatura_id={self.asignatura_id}, nota={self.nota})"
        )


class InstitutoDAO:
    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd

    def conectar(self):
        conexion = sqlite3.connect(self.nombre_bd)
        conexion.execute("PRAGMA foreign_keys = ON")
        return conexion

    def crear_tablas(self):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS alumnos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS asignaturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            horas INTEGER NOT NULL
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS matriculas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alumno_id INTEGER NOT NULL,
            asignatura_id INTEGER NOT NULL,
            nota REAL,
            FOREIGN KEY (alumno_id) REFERENCES alumnos(id) ON DELETE CASCADE,
            FOREIGN KEY (asignatura_id) REFERENCES asignaturas(id) ON DELETE CASCADE
        )
        """)

        con.commit()
        con.close()

    def insertar_alumno(self, alumno):
        con = self.conectar()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO alumnos (nombre, edad) VALUES (?, ?)",
            (alumno.nombre, alumno.edad)
        )

        alumno.id = cur.lastrowid
        con.commit()
        con.close()
        return alumno.id

    def insertar_asignatura(self, asignatura):
        con = self.conectar()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO asignaturas (nombre, horas) VALUES (?, ?)",
            (asignatura.nombre, asignatura.horas)
        )

        asignatura.id = cur.lastrowid
        con.commit()
        con.close()
        return asignatura.id

    def insertar_matricula(self, matricula):
        con = self.conectar()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO matriculas (alumno_id, asignatura_id, nota) VALUES (?, ?, ?)",
            (matricula.alumno_id, matricula.asignatura_id, matricula.nota)
        )

        matricula.id = cur.lastrowid
        con.commit()
        con.close()
        return matricula.id

    def obtener_alumnos(self):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("SELECT id, nombre, edad FROM alumnos")
        filas = cur.fetchall()
        con.close()

        return [Alumno(f[1], f[2], f[0]) for f in filas]

    def obtener_asignaturas(self):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("SELECT id, nombre, horas FROM asignaturas")
        filas = cur.fetchall()
        con.close()

        return [Asignatura(f[1], f[2], f[0]) for f in filas]

    def obtener_matriculas(self):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("SELECT id, alumno_id, asignatura_id, nota FROM matriculas")
        filas = cur.fetchall()
        con.close()

        return [Matricula(f[1], f[2], f[3], f[0]) for f in filas]

    def obtener_matriculas_detalladas(self):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("""
        SELECT m.id, a.nombre, s.nombre, m.nota
        FROM matriculas m
        JOIN alumnos a ON m.alumno_id = a.id
        JOIN asignaturas s ON m.asignatura_id = s.id
        ORDER BY a.nombre, s.nombre
        """)

        filas = cur.fetchall()
        con.close()

        return filas

    def obtener_asignaturas_de_alumno(self, id_alumno):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("""
        SELECT s.id, s.nombre, s.horas, m.nota
        FROM matriculas m
        JOIN asignaturas s ON m.asignatura_id = s.id
        WHERE m.alumno_id = ?
        ORDER BY s.nombre
        """, (id_alumno,))

        filas = cur.fetchall()
        con.close()

        return filas

    def obtener_alumnos_de_asignatura(self, id_asignatura):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("""
        SELECT a.id, a.nombre, a.edad, m.nota
        FROM matriculas m
        JOIN alumnos a ON m.alumno_id = a.id
        WHERE m.asignatura_id = ?
        ORDER BY a.nombre
        """, (id_asignatura,))

        filas = cur.fetchall()
        con.close()

        return filas

    def actualizar_nota(self, id_matricula, nueva_nota):
        con = self.conectar()
        cur = con.cursor()

        cur.execute(
            "UPDATE matriculas SET nota = ? WHERE id = ?",
            (nueva_nota, id_matricula)
        )

        con.commit()
        filas_modificadas = cur.rowcount
        con.close()

        return filas_modificadas

    def eliminar_alumno(self, id_alumno):
        con = self.conectar()
        cur = con.cursor()

        cur.execute("DELETE FROM alumnos WHERE id = ?", (id_alumno,))

        con.commit()
        filas_borradas = cur.rowcount
        con.close()

        return filas_borradas

def main():
    dao = InstitutoDAO("instituto.db")
    dao.crear_tablas()

    ana = Alumno("Ana", 20)
    luis = Alumno("Luis", 21)

    bd = Asignatura("Bases de Datos", 192)
    prog = Asignatura("Programación", 256)
    sistemas = Asignatura("Sistemas Informáticos", 160)

    ana.id = dao.insertar_alumno(ana)
    luis.id = dao.insertar_alumno(luis)

    bd.id = dao.insertar_asignatura(bd)
    prog.id = dao.insertar_asignatura(prog)
    sistemas.id = dao.insertar_asignatura(sistemas)

    dao.insertar_matricula(Matricula(ana.id, bd.id, 8.5))
    dao.insertar_matricula(Matricula(ana.id, prog.id, 9.0))
    dao.insertar_matricula(Matricula(luis.id, bd.id, 7.0))
    dao.insertar_matricula(Matricula(luis.id, sistemas.id, 6.5))

    print("=== ALUMNOS ===")
    for alumno in dao.obtener_alumnos():
        print(alumno)

    print("\n=== ASIGNATURAS ===")
    for asignatura in dao.obtener_asignaturas():
        print(asignatura)

    print("\n=== MATRÍCULAS DETALLADAS ===")
    for fila in dao.obtener_matriculas_detalladas():
        print(fila)

    print("\n=== ASIGNATURAS DE ANA ===")
    for fila in dao.obtener_asignaturas_de_alumno(ana.id):
        print(fila)

    print("\n=== ALUMNOS DE BASES DE DATOS ===")
    for fila in dao.obtener_alumnos_de_asignatura(bd.id):
        print(fila)

if __name__ == "__main__":
    main()