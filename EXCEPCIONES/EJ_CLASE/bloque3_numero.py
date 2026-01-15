try:
    numero = int(input("Introduce un número positivo: "))
    if numero <= 0:
        raise ValueError("El número debe ser positivo")
    if numero > 100:
        raise ValueError("El número no puede ser mayor de 100")
    if numero % 2 != 0:
        raise ValueError("El numero debe de ser par")
except ValueError as e:
    print("Error:", e)
else:
    print("El cuadrado es:", numero ** 2)
finally:
    print("Fin del programa")