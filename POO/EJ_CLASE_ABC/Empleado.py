from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def salario(self):
        pass

class EmpleadoFijo(Empleado):
    def __init__(self, salario_base):
        self.salario_base = salario_base
    def salario(self):
        return self.salario_base

class EmpleadoPorHoras(Empleado):
    def __init__(self, horas, precio):
        self.horas = horas
        self.precio = precio
    def salario(self):
        return self.precio * self.horas

class Comisionista(Empleado):
    def __init__(self, ventas, porcentaje):
        self.ventas = ventas
        self.porcentaje = porcentaje
    def salario(self):
        return self.ventas * self.porcentaje

def main():
    fijo = EmpleadoFijo(1200)
    print(f"El salario del trabajador fijo es: {fijo.salario()}")
    eHoras = EmpleadoPorHoras(100, 50)
    print(f"El salario del trabajador por horas es: {eHoras.salario()}")
    comisionista = Comisionista(10000, 0.20)
    print(f"El salario del comisionista es: {comisionista.salario()}")

if __name__ == "__main__":
    main()
