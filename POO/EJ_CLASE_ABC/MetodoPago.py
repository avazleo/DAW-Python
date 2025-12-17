from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, cantidad: float) -> None:
        ...
    @property
    @abstractmethod
    def tipo(self) -> str:
        ...

class TarjetaCredito(MetodoPago):
    def __init__(self, tarjeta) -> None:
        self.__tipo = "Tarjeta de credito"
        self.__tarjeta = tarjeta

    def pagar(self, cantidad: float) -> None:
        return f"Pagando {cantidad:.2f}€ con la tarjeta {self.__tarjeta}"

    @property
    def tipo(self) -> str:
        return self.__tipo

class Bizum(MetodoPago):
    def __init__(self, telefono) -> None:
        self.__tipo = "Bizum"
        self.__telefono = telefono

    def pagar(self, cantidad: float) -> None:
        return f"Pagando {cantidad:.2f}€ con el telefono {self.__telefono}"

    @property
    def tipo(self) -> str:
        return self.__tipo

class PayPal(MetodoPago):
    def __init__(self, email) -> None:
        self.__tipo = "PayPal"
        self.__email = email

    def pagar(self, cantidad: float) -> None:
        return f"Pagando {cantidad:.2f}€ con el email {self.__email}"

    @property
    def tipo(self) -> str:
        return self.__tipo

def main():
    metodos = [TarjetaCredito(5049459030345), Bizum(666666666), PayPal("correo@correo.ja")]
    for metodo in metodos:
        print(f"Usando método: {metodo.tipo}")
        print(metodo.pagar(50))

if __name__ == "__main__":
    main()