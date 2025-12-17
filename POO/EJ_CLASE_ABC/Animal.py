from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Animal(ABC):
    @abstractmethod
    def hablar(self) -> str: pass

class Perro(Animal):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__specie = "Perro"

    @property
    def specie(self) -> str:
        return self.__specie

    @specie.setter
    def specie(self, nombre: str):
        pass

    def hablar(self) -> str:
        return "Guau"

    def __str__(self) -> str:
        return f"El perro {self.nombre}"

class Gato(Animal):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__specie = "Gato"

    @property
    def specie(self) -> str:
        return self.__specie

    @specie.setter
    def specie(self, nombre: str):
        pass

    def hablar(self) -> str:
        return "Miau"

    def __str__(self) -> str:
        return f"El gato {self.nombre}"

class Vaca(Animal):
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.__specie = "Vaca"

    @property
    def specie(self) -> str:
        return self.__specie

    @specie.setter
    def specie(self, nombre: str):
        pass

    def hablar(self) -> str:
        return "Muuu"

    def __str__(self) -> str:
        return f"La vaca {self.nombre}"

def main() -> None:
    animales = [Perro("Rantamplan"), Gato("Oku"), Vaca("Que rie")]

    for animal in animales:
        print(f"{animal} dice {animal.hablar()}")

if __name__ == "__main__":
    main()


