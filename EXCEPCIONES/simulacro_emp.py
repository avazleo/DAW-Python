# ------------------------------
# SOLUCIÓN (1º DAW) - Herencia + Excepciones + Diccionarios + Bucles
# ------------------------------
class SalarioInvalidoError(Exception):
#Se lanza cuando algún dato económico no es válido.
    pass

class Empleado:
    def __init__(self, id_empleado: int, nombre: str, salario_base: float):
        if salario_base < 0:
            raise SalarioInvalidoError("El salario base no puede ser negativo.")
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.salario_base = float(salario_base)

    def calcular_salario(self) -> float:
    # En la clase base, devuelve exclusivamente el salario base
        return self.salario_base

    def __str__(self) -> str:
        return f"[{self.id_empleado}] {self.nombre}"

class EmpleadoHoras(Empleado):
    def __init__(self, id_empleado: int, nombre: str, horas_trabajadas: float, precio_hora: float):
        if horas_trabajadas < 0:
            raise SalarioInvalidoError("Las horas trabajadas no pueden ser negativas.")
        if precio_hora <= 0:
            raise SalarioInvalidoError("El precio por hora debe ser mayor que 0.")
        # salario_base no se usa en este tipo, lo dejamos a 0
        super().__init__(id_empleado, nombre, 0)
        self.horas_trabajadas = float(horas_trabajadas)
        self.precio_hora = float(precio_hora)

    def calcular_salario(self) -> float:
    # Sobrescritura: horas * precio
        return self.horas_trabajadas * self.precio_hora

class EmpleadoFijo(Empleado):
    def __init__(self, id_empleado: int, nombre: str, salario_base: float, complementos: dict):
        super().__init__(id_empleado, nombre, salario_base)
        # complementos: {"transporte": 100, "productividad": 150, ...}
        self.complementos = complementos

    def calcular_salario(self) -> float:
    # Sobrescritura: salario base + suma de complementos (recorriendo diccionario con for)
        total = self.salario_base
        for concepto, cantidad in self.complementos.items():
            total += float(cantidad)
        return total

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Añadir empleado por horas")
    print("2. Añadir empleado fijo")
    print("3. Mostrar salarios")
    print("4. Salir")

def main():
    empleados = {} # clave: id_empleado, valor: objeto empleado
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            try:
            # Añadir empleado por horas (con try/except)
                id_emp = int(input("ID: "))
                nombre = input("Nombre: ")
                horas = float(input("Horas trabajadas: "))
                precio = float(input("Precio por hora: "))
                emp = EmpleadoHoras(id_emp, nombre, horas, precio)
                empleados[id_emp] = emp
                print("■ Empleado por horas añadido.")
            except ValueError:
                print("■ Error: debes introducir números válidos (ID entero, horas y precio numéricos")
            except SalarioInvalidoError as e:
                print(f"■ Error de datos: {e}")

        elif opcion == "2":
            # Añadir empleado fijo (con try/except)
            try:
                id_emp = int(input("ID: "))
                nombre = input("Nombre: ")
                salario_base = float(input("Salario base: "))
                # Pedimos complementos con un bucle while
                complementos = {}
                print("Introduce complementos (vacío para terminar).")
                while True:
                    concepto = input("Concepto (enter para salir): ").strip()
                    if concepto == "":
                        break
                    cantidad = float(input(f"Cantidad para '{concepto}': "))
                    complementos[concepto] = cantidad
                emp = EmpleadoFijo(id_emp, nombre, salario_base, complementos)
                empleados[id_emp] = emp
                print("■ Empleado fijo añadido.")
            except ValueError:
                print("■ Error: salario y complementos deben ser números válidos.")
            except SalarioInvalidoError as e:
                print(f"■ Error de datos: {e}")

        elif opcion == "3":
        # Mostrar salarios (recorrer diccionario con for)
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print("\n--- SALARIOS ---")
                for id_emp, emp in empleados.items():
                    print(f"{emp} | Tipo: {emp.__class__.__name__} | Salario: {emp.calcular_salario()}")
        
        elif opcion == "4":
            print("Saliendo...")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()