import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="empresa"
)

cursor = conexion.cursor()

cursor.execute("SELECT * FROM empleados")

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conexion.close()