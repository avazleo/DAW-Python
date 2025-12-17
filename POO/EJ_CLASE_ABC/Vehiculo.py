from abc import ABC, abstractmethod

class Vehiculo(ABC):

    @property
    @abstractmethod
    def ruedas(self) -> int:
        pass

    @abstractmethod
    def arrancar(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Moto(Vehiculo):
    def __init__(self) -> None:
        self.encendido = False

    @property
    def ruedas(self) -> int:
        return 2
    def arrancar(self) -> bool:
        self.encendido = True
    def detener(self):
        self.encendido = False
    def info(self):
        return f"La moto está {'Arrancada' if self.encendido else 'Apagada'} y tiene {self.ruedas} ruedas"

class Coche(Vehiculo):
    def __init__(self):
        self.encendido = False

    @property
    def ruedas(self) -> int:
        return 4
    def arrancar(self):
        self.encendido = True
    def detener(self):
        self.encendido = False
    def info(self):
        return f"El coche está {'Arrancada' if self.encendido else 'Apagada'} y tiene {self.ruedas} ruedas"

class Camion(Vehiculo):
    def __init__(self):
        self.encendido = False

    @property
    def ruedas(self) -> int:
        return 6
    def arrancar(self):
        self.encendido = True
    def detener(self):
        self.encendido = False
    def info(self):
        return f"El camión está {'Arrancada' if self.encendido else 'Apagada'} y tiene {self.ruedas} ruedas"


def main():
    vehiculos = [Moto(), Coche(), Camion()]
    for vehiculo in vehiculos:
        vehiculo.arrancar()
        print(vehiculo.info())
        vehiculo.detener()
        print(vehiculo.info())

if __name__ == "__main__":
    main()
