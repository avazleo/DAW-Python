try:
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    print("Resultado:", a / b)
except ZeroDivisionError:
    print("Error: no se puede dividir entre cero")
except ValueError:
    print("Error: introduce valores numéricos")