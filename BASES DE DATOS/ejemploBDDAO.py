import sqlite3

class Libro:

    def __init__(self, titulo, autor, anio, id=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f"Libro(id={self.id}, titulo='{self.titulo}', autor='{self.autor}', anio={self.anio})"


class LibroDAO:

    def __init__(self, nombre_bd):
        self.nombre_bd = nombre_bd

    def _conectar(self):
        return sqlite3.connect(self.nombre_bd)

    def crear_tabla(self):

        conexion = self._conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            anio INTEGER NOT NULL
        )
        """)

        conexion.commit()
        conexion.close()

    def insertar(self, libro):

        conexion = self._conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO libros (titulo, autor, anio) VALUES (?, ?, ?)",
            (libro.titulo, libro.autor, libro.anio)
        )

        conexion.commit()
        conexion.close()

    def obtener_todos(self):

        conexion = self._conectar()
        cursor = conexion.cursor()

        cursor.execute("SELECT id,titulo,autor,anio FROM libros")

        filas = cursor.fetchall()

        conexion.close()

        libros=[]

        for fila in filas:
            libros.append(Libro(fila[1],fila[2],fila[3],fila[0]))

        return libros

    def buscar_por_titulo(self,texto):

        conexion=self._conectar()
        cursor=conexion.cursor()

        cursor.execute(
            "SELECT id,titulo,autor,anio FROM libros WHERE titulo LIKE ?",
            ("%"+texto+"%",)
        )

        filas=cursor.fetchall()

        conexion.close()

        libros=[]

        for fila in filas:
            libros.append(Libro(fila[1],fila[2],fila[3],fila[0]))

        return libros

    def actualizar_anio(self,id_libro,nuevo_anio):

        conexion=self._conectar()
        cursor=conexion.cursor()

        cursor.execute(
            "UPDATE libros SET anio=? WHERE id=?",
            (nuevo_anio,id_libro)
        )

        conexion.commit()

        filas=cursor.rowcount

        conexion.close()

        return filas

    def eliminar(self,id_libro):

        conexion=self._conectar()
        cursor=conexion.cursor()

        cursor.execute(
            "DELETE FROM libros WHERE id=?",
            (id_libro,)
        )

        conexion.commit()

        filas=cursor.rowcount

        conexion.close()

        return filas

dao = LibroDAO("biblioteca.db")

dao.crear_tabla()

dao.insertar(Libro("1984","George Orwell",1949))
dao.insertar(Libro("El Quijote","Miguel de Cervantes",1605))
dao.insertar(Libro("Dune","Frank Herbert",1965))

print("Libros insertados")

libros = dao.obtener_todos()

for libro in libros:
    print(libro)

resultados = dao.buscar_por_titulo("Du")
print("Libros buscados")

for libro in resultados:
    print(libro)

dao.actualizar_anio(1,1950)

print("Libros actualizados")
for libro in dao.obtener_todos():
    print(libro)


dao.eliminar(2)