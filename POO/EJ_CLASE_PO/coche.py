class Coche:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        print(f"El coche es de la marca: {self.marca}, modelo: {self.modelo}, año: {self.anio}")


def main():
    marca = input("Ingrese marca: ")
    modelo = input("Ingrese modelo: ")
    anio = input("Ingrese año: ")
    coche = Coche(marca, modelo, anio)
    coche.descripcion()

if __name__ == "__main__":
    main()
