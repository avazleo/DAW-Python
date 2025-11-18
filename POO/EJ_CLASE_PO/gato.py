class Gato:
    def __init__(self, nombre):
        self.nombre = nombre

    def maullar(self):
        print(f"Miau, soy {self.nombre}")

def main():
    nombre = input("Ingresa el nombre de tu gato: ")
    gato = Gato(nombre)
    gato.maullar()

if __name__ == "__main__":
    main()
