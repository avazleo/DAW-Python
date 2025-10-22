# Inicializamos contadores
positive_counter = 0
negative_counter = 0
zeros_counter = 0

# Pedimos cantidad de números a introducir
total_numbers = int(input("¿Cuántos números vas a introducir?: "))

# Ciclo
for i in range(total_numbers):
    number = int(input(f"Número {i + 1}: "))
    # Comprobamos si es +, - ó 0 e incrementamos contador
    if number > 0:
        positive_counter += 1
    elif number < 0:
        negative_counter += 1
    else:
        zeros_counter += 1

# Mostramos resultados
print(f"Números positivos: {positive_counter}")
print(f"Números negativos: {negative_counter}")
print(f"Números igual a 0: {zeros_counter}")