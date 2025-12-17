from abc import ABC, abstractmethod

class Electrodomestico(ABC):
    @property
    @abstractmethod
    def marca(self) -> str:
        pass
    @property
    @abstractmethod
    def modelo(self) -> str:
        pass
    @abstractmethod
    def consumo(self) -> float:
        pass

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self) -> str:
        return self.__marca

    @property
    def modelo(self) -> str:
        return self.__modelo
    def consumo(self) -> float:
        return 1.2

class Televisor(Electrodomestico):
    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self) -> str:
        return self.__marca
    @property
    def modelo(self) -> str:
        return self.__modelo
    def consumo(self) -> float:
        return 0.3

class Microondas(Electrodomestico):
    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca = marca
        self.__modelo = modelo

    @property
    def marca(self) -> str:
        return self.__marca
    @property
    def modelo(self) -> str:
        return self.__modelo
    def consumo(self) -> float:
        return 3.1

def main():
    electrodomesticos = [Lavadora("LG", "L3421"), Televisor("LG", "G3421"), Microondas("LG", "M3421")]
    for electrodomestico in electrodomesticos:
        print(f"El consumo del {electrodomestico.marca} y modelo: {electrodomestico.modelo} es de {electrodomestico.consumo()}")

if __name__ == "__main__":
    main()