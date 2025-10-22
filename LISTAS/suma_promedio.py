# Suma y promedio. A partir de una lista de números
# introducidos por el usuario, calcula:
# a) La suma de todos los elementos.
# b) El valor promedio.

numbers = []
print("Introduce números hasta que escribas FIN")

while True:
    data = input("Introduce un número (FIN para terminar): ")
    if data == "FIN":
        break
    numbers.append(int(data))

sum = sum(numbers)
average = sum / len(numbers)

print(f"La suma de los números es: {sum} y su media es: {average}")
