# Invertir lista. Dada una lista de números, genera otra lista con los elementos en orden inverso
# (usando slicing y manualmente con bucles)

numbers = [1,2,3,4,5,6,7,8,9]

# Usando slicing
numbers_reverse = numbers[::-1]

# Usando bucle
num_reverse_loop =[]
for num in range(len(numbers)-1,-1,-1):
    num_reverse_loop.append(numbers[num])

print(f"El resultado de la lista inversa con slicing es: {numbers_reverse}")
print(f"El resultado de la lista inversa con bucle es: {num_reverse_loop}")

