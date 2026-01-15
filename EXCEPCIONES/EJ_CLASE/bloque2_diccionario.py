usuarios = {
"ana": 23,
"luis": 30,
"maria": 19
}
try:
    nombre = input("Introduce el usuario: ")
    print("Edad:", usuarios[nombre])
except KeyError:
    print("El usuario no existe")
