try:
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if len(contraseña) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")
    print("Registro correcto")
except ValueError as e:
    print("Error:", e)