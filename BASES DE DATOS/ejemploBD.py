import sqlite3

conexion = sqlite3.connect("empresa.db")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER
)
""")

cursor.execute(
    "INSERT INTO empleados (nombre, edad) VALUES (?, ?)",
    ("Ana", 30)
)

conexion.commit()

cursor.execute("SELECT * FROM empleados")

for fila in cursor.fetchall():
    print(fila)

conexion.close()