# ------------------------------------------------------------
# SOLUCIÓN - Gestión de Vehículos (1º DAW)
# Evalúa: herencia, sobrescritura, diccionarios, bucles y try/except
# ------------------------------------------------------------

class PrecioInvalidoError(Exception):
    """Se lanza cuando algún dato económico no es válido."""
    pass


class Vehiculo:
    def __init__(self, matricula: str, marca: str, precio_base_dia: float):
        if precio_base_dia < 0:
            raise PrecioInvalidoError("El precio base por día no puede ser negativo.")
        self.matricula = matricula
        self.marca = marca
        self.precio_base_dia = float(precio_base_dia)

    def calcular_precio(self) -> float:
        # En la clase base: devuelve exclusivamente el precio base por día
        return self.precio_base_dia

    def __str__(self) -> str:
        return f"[{self.matricula}] {self.marca}"


class VehiculoPorDias(Vehiculo):
    def __init__(self, matricula: str, marca: str, precio_base_dia: float, dias_alquiler: int):
        if dias_alquiler <= 0:
            raise PrecioInvalidoError("Los días de alquiler deben ser mayores que 0.")
        super().__init__(matricula, marca, precio_base_dia)
        self.dias_alquiler = int(dias_alquiler)

    def calcular_precio(self) -> float:
        # Sobrescritura: precio base * días
        return self.precio_base_dia * self.dias_alquiler


class VehiculoPremium(Vehiculo):
    def __init__(self, matricula: str, marca: str, precio_base_dia: float, dias_alquiler: int, extras: dict):
        if dias_alquiler <= 0:
            raise PrecioInvalidoError("Los días de alquiler deben ser mayores que 0.")

        super().__init__(matricula, marca, precio_base_dia)
        self.dias_alquiler = int(dias_alquiler)
        # Validación de extras: no se permiten costes negativos
        for concepto, coste in extras.items():
            if float(coste) < 0:
                raise PrecioInvalidoError(f"El extra '{concepto}' tiene un coste negativo.")
        self.extras = extras  # {"gps": 5, "silla_bebe": 7, ...}

    def calcular_precio(self) -> float:
        # Sobrescritura: (precio base + suma de extras) x dias_alquiler (recorrer diccionario con for)
        total = self.precio_base_dia
        for concepto, coste in self.extras.items():
            total += float(coste)
        total *= self.dias_alquiler
        return total


def mostrar_menu() -> None:
    print("\n--- MENÚ ---")
    print("1. Añadir vehículo por días")
    print("2. Añadir vehículo premium")
    print("3. Mostrar precios de alquiler")
    print("4. Salir")


def main() -> None:
    vehiculos = {}  # clave: matricula, valor: objeto Vehiculo

    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            # Alta de VehiculoPorDias (con try/except)
            try:
                matricula = input("Matrícula: ").strip()
                marca = input("Marca: ").strip()
                precio_base = float(input("Precio base por día: "))
                dias = int(input("Días de alquiler: "))

                v = VehiculoPorDias(matricula, marca, precio_base, dias)
                vehiculos[matricula] = v
                print("OK: vehículo por días añadido.")
            except ValueError:
                print("ERROR: precio debe ser numérico y días debe ser un entero.")
            except PrecioInvalidoError as e:
                print(f"ERROR de datos: {e}")

        elif opcion == "2":
            # Alta de VehiculoPremium (con try/except)
            try:
                matricula = input("Matrícula: ").strip()
                marca = input("Marca: ").strip()
                precio_base = float(input("Precio base por día: "))
                dias = int(input("Días de alquiler: "))

                # Pedimos extras con un bucle while
                extras = {}
                print("Introduce extras (vacío para terminar).")
                while True:
                    concepto = input("Extra (enter para salir): ").strip()
                    if concepto == "":
                        break
                    coste = float(input(f"Coste de '{concepto}': "))
                    extras[concepto] = coste

                v = VehiculoPremium(matricula, marca, precio_base, dias, extras)
                vehiculos[matricula] = v
                print("OK: vehículo premium añadido.")
            except ValueError:
                print("ERROR: el precio y los costes de extras deben ser números válidos.")
            except PrecioInvalidoError as e:
                print(f"ERROR de datos: {e}")

        elif opcion == "3":
            # Mostrar precios (for sobre diccionario)
            if not vehiculos:
                print("No hay vehículos registrados.")
            else:
                print("\n--- PRECIOS ---")
                for matricula, v in vehiculos.items():
                    print(f"{v} | Tipo: {v.__class__.__name__} | Precio: {v.calcular_precio():.2f}")

        elif opcion == "4":
            print("Saliendo...")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
