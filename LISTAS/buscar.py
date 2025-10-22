# Buscar elemento: Pide una lista de palabras al usuario.
# Pregunta por una palabra y di si está en la lista y en qué posición aparece.

works = []
print("Introduce palabras hasta que escribas un punto (.)")

while True:
    data = input("Introduce un número (punto (.) para terminar): ")
    if data == ".":
        break
    works.append(data)

work = input("Introduce una palabra a buscar en la lista: ")

if work in works:
    index = works.index(work)
    print(f"La palabra {work} existe en la lista en la posicion {index}")
else:
    print(f"La palabra {work} no existe en la lista")



