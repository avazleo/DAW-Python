# Programa que comprueba si una palabra es palíndroma

# Pedimos una palabra al usuario
palabra = input("Introduce una palabra: ")

# Convertimos la palabra a minúsculas (para evitar problemas con mayúsculas)
palabra = palabra.lower()

# Obtenemos la palabra al revés usando slicing
invertida = palabra[::-1]

# Mostramos ambas para comprobar
print("Palabra original:", palabra)
print("Palabra invertida:", invertida)

# Comprobamos si son iguales
if palabra == invertida:
    print("La palabra es palíndroma.")
else:
    print("La palabra NO es palíndroma.")