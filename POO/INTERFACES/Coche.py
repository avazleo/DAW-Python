from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @property
    @abstractmethod
    def velocidad(self) -> float:
        """km/h actuales"""
        ...

    @abstractmethod
    def arrancar(self) -> None: ...
    @abstractmethod
    def detener(self) -> None: ...
    @abstractmethod
    def acelerar(self, n: float) -> None: ...
    @abstractmethod
    def frenar(self, n: float) -> None: ...

class Coche(Vehiculo):
    def __init__(self) -> None:
        self._velocidad = 0.0
        self._encendido = False

    @property
    def velocidad(self) -> float:
        return self._velocidad

    def arrancar(self) -> None:
        self._encendido = True

    def detener(self) -> None:
        self._encendido = False
        self._velocidad = 0.0

    def acelerar(self, n: float) -> None:
        if self._encendido:
            self._velocidad += n

    def frenar(self, n: float) -> None:
        self._velocidad = max(0.0, self._velocidad - n)

class Bicicleta(Vehiculo):
    def __init__(self) -> None:
        self._velocidad = 0.0

    @property
    def velocidad(self) -> float:
        return self._velocidad

    def arrancar(self) -> None:
        pass  # no aplica, pero existe el método

    def detener(self) -> None:
        self._velocidad = 0.0

    def acelerar(self, n: float) -> None:
        self._velocidad += n

    def frenar(self, n: float) -> None:
        self._velocidad = max(0.0, self._velocidad - n)

def prueba(v: Vehiculo) -> None:
    v.arrancar()
    v.acelerar(10)
    v.frenar(3)
    print(v.velocidad)

if __name__ == "__main__":
    # v = Vehiculo()  # ❌ TypeError: clase abstracta, no se puede instanciar
    coche = Coche()
    bici = Bicicleta()
    prueba(coche)  # 7.0
    prueba(bici)   # 7.0