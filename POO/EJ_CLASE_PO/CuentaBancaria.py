class CuentaBancaria:
    def __init__(self, saldo_inicial=0.0):
        # saldo privado
        self.__saldo = float(saldo_inicial) if saldo_inicial >= 0 else 0.0
        if saldo_inicial < 0:
            print("⚠️ Saldo inicial negativo, ajustado a 0.0")

    def depositar(self, cantidad: float) -> bool:
        """Ingresa dinero. Devuelve True si tuvo éxito; False si la cantidad no es válida."""
        if cantidad is None or cantidad <= 0:
            print("⚠️ La cantidad a depositar debe ser positiva.")
            return False
        self.__saldo += cantidad
        return True

    def retirar(self, cantidad: float) -> bool:
        """Retira dinero. Devuelve True si tuvo éxito; False si no hay fondos o cantidad inválida."""
        if cantidad is None or cantidad <= 0:
            print("⚠️ La cantidad a retirar debe ser positiva.")
            return False
        if cantidad > self.__saldo:
            print("⚠️ Fondos insuficientes. Operación cancelada.")
            return False
        self.__saldo -= cantidad
        return True

    def mostrar_saldo(self) -> float:
        return self.__saldo

def main():
    cuenta = CuentaBancaria(100)
    print(f"El saldo de mi cuenta es: {cuenta.mostrar_saldo():.2f}€")
    cuenta.depositar(100)
    print(f"El saldo de mi cuenta es: {cuenta.mostrar_saldo():.2f}€")
    cuenta.retirar(300)
    cuenta.retirar(-20)
    cuenta.retirar(35)
    print(f"El saldo de mi cuenta es: {cuenta.mostrar_saldo():.2f}€")


if __name__ == "__main__":
    main()
