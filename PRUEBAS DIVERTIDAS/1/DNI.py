# Programa para comprobar si la letra del DNI es correcta

# Lista con las letras válidas según el resto de dividir el número entre 23
letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X",
          "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

# Pedimos el DNI (por ejemplo: 12345678Z)
dni = input("Introduce tu DNI (8 números y una letra): ")

# Separar el número de la letra usando slicing
numero = int(dni[:8])
letra = dni[8].upper()   # convertimos a mayúscula por si el usuario pone minúscula

# Calculamos la letra que debería tener el DNI
letra_correcta = letras[numero % 23]

# Comprobamos si la letra es correcta
if letra == letra_correcta:
    print("La letra del DNI es correcta.")
else:
    print("La letra del DNI no es correcta. Debería ser:", letra_correcta)