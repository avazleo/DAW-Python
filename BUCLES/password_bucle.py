# Crear un programa que pida contraseñas hasta que el usuario
# escriba la correccta

password = "NoEs1234"

while True:
    password_user = input("Ingrese su password: ")
    if password_user == password:
        print(f"Contraseña correcta. Bienvenido a casa!")
        break
    else:
        print(f"La contraseña introducida no es correcta, pruebe otra vez")

coincide = False

while not coincide:
    password_user = input("Ingrese su password: ")
    if password_user == password:
        print(f"Contraseña correcta. Bienvenido a casa!")
        coincide = True
    else:
        print(f"La contraseña introducida no es correcta, pruebe otra vez")
