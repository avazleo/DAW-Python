# Crear y mostrar. Pide al usuario que introduzca
# 5 números enteros y guárdalos en una lista.
# Muestra luego la lista completa y su longitud.

print("Introduce 5 números:")
numbers = []
for i in range(5):
    num = int(input(f"Introduce el {i + 1}: "))
    numbers.append(num)

print(f"La lista completa es: {numbers} y su longitud es: {len(numbers)}")
