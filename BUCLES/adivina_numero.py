# Juego de adivinanza: el programa genera un número aleatorio
# entre 1 y 100 y el usuario debe adivinarlo.
# El programa debe dar pistas: "más alto" o "más bajo"

#Importamos la liberia random
import random

#Generamos el número aleatorio a adivinar entre 1 y 100
numero = random.randint(1, 100)

#Ciclo para adivinar el número
while True:
    num_user = int(input("Ingrese un numero: "))
    if num_user == numero:
        print(f"El numero {num_user} es correcto!")
        break
    elif num_user > numero:
        print(f"Más bajo")
    else:
        print(f"Más alto")


