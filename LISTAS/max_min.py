#Máximo y mínimo. Dada una lista de números, encuentra el mayor y el menor sin usar max() ni min().

numbers = []
print("Introduce números hasta que escribas FIN")

while True:
    data = input("Introduce un número (FIN para terminar): ")
    if data == "FIN":
        break
    numbers.append(int(data))

max = numbers[0]
min = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]

print(f"El valor máximo es: {max} y el valor minimo es: {min}")