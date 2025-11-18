class Vehiculo:
    def __init__(self, marca, ruedas):
        self.marca = marca
        self.ruedas = ruedas

    def __str__(self):
        return f"{self.marca} con {self.ruedas} ruedas"

class Bicicleta(Vehiculo):
    def __init__(self, marca, tipo):
        super().__init__(marca, ruedas=2)
        self.tipo = tipo

    def __str__(self):
        base = super().__str__()
        return f"{base} (tipo: {self.tipo})"

def main():
    vehiculo = Vehiculo("Nissan", 4)
    print(vehiculo)

    bicicleta = Bicicleta("BH", "Montaña")
    print(bicicleta)

if __name__ == "__main__":
    main()

