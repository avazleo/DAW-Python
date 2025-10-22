# Programa que pide números hasta que el usuario escribe
# un número negativo. AL final, muestra la suma de todos
# los números introducidos

sumador = 0

while True:
    numero = int(input("Ingrese un numero: "))
    if numero < 0:
        break
    sumador += numero

print(f"La suma de todos los números introducidos es: {sumador}")
