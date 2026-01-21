try:
    with open("logs.txt","w") as f:
        print("Escribe todos los mensajes que quieras para el logs ('salir' para terminar)")
        while True:
            mensaje = input()
            if mensaje.lower() == "salir":
                break
            f.write(mensaje + "\n")
except IOError:
    print("Error al escribir el fichero")