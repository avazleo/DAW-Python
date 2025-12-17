from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Figura(ABC):
    @abstractmethod
    def area(self) -> float:
        pass
    @abstractmethod
    def perimetro(self) -> float:
        pass

class Cuadrado(Figura):
    def __init__(self, lado: float) -> None:
        self.lado = lado

    def area(self) -> float:
        return self.lado**2

    def perimetro(self) -> float:
        return 2*self.lado


class Rectangulo(Figura):
    def __init__(self, alto: float, ancho: float) -> None:
        self.alto = alto
        self.ancho = ancho

    def area(self) -> float:
        return self.alto*self.ancho

    def perimetro(self) -> float:
        return 2*self.alto+self.ancho

def main() -> None:
    cuadrado = Cuadrado(2.5)
    print(f"El area de cuadrado es: {cuadrado.area()}")
    print(f"El perimetro de cuadrado es: {cuadrado.perimetro()}")
    rectangulo = Rectangulo(3.0, 4.0)
    print(f"El area de rectangulo es: {rectangulo.area()}")
    print(f"El perimetro de rectangulo es: {rectangulo.perimetro()}")

if __name__ == '__main__':
    main()
