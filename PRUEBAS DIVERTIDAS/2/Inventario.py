class Libro:
    """Representa un libro con encapsulamiento estricto (Doble guion bajo)."""

    def __init__(self, titulo: str, autor: str, isbn: str, copias: int):
        self.titulo = titulo
        self.autor = autor
        self.__isbn = "0000000000000"  # Valor por defecto si la asignación falla
        self.__copias_disponibles = copias

        # El constructor llama al setter para validar el ISBN inicial
        self.isbn = isbn

        # --- MÉTODO DE ACCESO (GETTER y SETTER) para isbn ---

    @property
    def isbn(self):
        """Getter para __isbn."""
        return self.__isbn

    @isbn.setter
    def isbn(self, nuevo_isbn: str):
        """Setter para __isbn con validación."""
        if len(nuevo_isbn) == 13 and nuevo_isbn.isdigit():
            self.__isbn = nuevo_isbn
        else:
            # Emite mensaje de error y mantiene el valor anterior (o el defecto si es la inicialización)
            print(
                f"❌ ERROR: ISBN '{nuevo_isbn}' no válido para '{self.titulo}'. Se mantuvo el valor original '{self.__isbn}'.")

    # --- MÉTODO DE ACCESO (GETTER) para copias_disponibles ---
    @property
    def copias_disponibles(self):
        """Getter para __copias_disponibles."""
        return self.__copias_disponibles

    # --- MÉTODOS PÚBLICOS DE STOCK ---
    def incrementar_copias(self, cantidad):
        """Aumenta las copias disponibles y devuelve el nuevo total."""
        if cantidad > 0:
            self.__copias_disponibles += cantidad
        return self.__copias_disponibles

    def decrementar_copias(self, cantidad):
        """Disminuye las copias. Devuelve el nuevo total o -1 si no hay stock."""
        if self.__copias_disponibles >= cantidad:
            self.__copias_disponibles -= cantidad
            return self.__copias_disponibles
        return -1

    def __str__(self):
        """Representación legible del objeto Libro."""
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.__isbn}, Copias: {self.__copias_disponibles}"


class Inventario:
    """Gestiona la colección de objetos Libro con el atributo de colección privado."""

    def __init__(self):
        # ATRIBUTO ESTRICTAMENTE PRIVADO
        self.__coleccion_libros = []

    @property
    def coleccion_libros(self):
        return self.__coleccion_libros

    def agregar_libro(self, libro):
        """Añade un libro, o incrementa las copias si ya existe (usando for)."""
        encontrado = None
        for libro_existente in self.__coleccion_libros:
            if libro_existente.isbn == libro.isbn:
                encontrado = libro_existente
                break

        if encontrado:
            copias_anadidas = libro.copias_disponibles
            nuevo_total = encontrado.incrementar_copias(copias_anadidas)
            return f"✅ Libro ya existente: '{libro.titulo}'. Se añadieron {copias_anadidas} copias. Total: {nuevo_total}"
        else:
            self.__coleccion_libros.append(libro)
            return f"➕ Libro nuevo añadido: '{libro.titulo}'. Copias iniciales: {libro.copias_disponibles}"

    def alquilar_copia(self, titulo_o_isbn):
        """Busca y decrementa una copia por título o ISBN (usando for)."""
        for libro in self.__coleccion_libros:
            if libro.titulo.lower() == titulo_o_isbn.lower() or libro.isbn == titulo_o_isbn:
                nuevo_stock = libro.decrementar_copias(1)

                if nuevo_stock != -1:
                    return libro
                else:
                    return f"❌ No hay copias disponibles de '{libro.titulo}'. (Stock: {libro.copias_disponibles})"

        return f"❌ Libro o ISBN no encontrado: '{titulo_o_isbn}'."

    def devolver_copia(self, isbn):
        """Busca y aumenta una copia por ISBN (usando for)."""
        for libro in self.__coleccion_libros:
            if libro.isbn == isbn:
                nuevo_total = libro.incrementar_copias(1)
                return f"⬅️ Devuelto: Una copia de '{libro.titulo}' ha sido recibida. Total: {nuevo_total}"

        return f"❌ Devolución fallida: No se encontró ningún libro con el ISBN: {isbn}"

    def listar_libros_disponibles(self):
        """Devuelve una lista de cadenas de texto (str) de los libros con existencias > 0."""
        libros_disponibles = []
        for libro in self.__coleccion_libros:
            if libro.copias_disponibles > 0:
                libros_disponibles.append(str(libro))
        return libros_disponibles


# ====================================================================
# FUNCIÓN DE CONTROL PRINCIPAL
# ====================================================================

def menu(inventario: Inventario):
    """Muestra un menú interactivo y ejecuta las opciones."""

    opcion = None

    # Bucle WHILE obligatorio para ejecución indefinida hasta Salir
    while opcion != "5":
        print("\n=== MENÚ DE GESTIÓN DE INVENTARIO ===")
        print("1. Listar libros disponibles")
        print("2. Alquilar libro (por Título/ISBN)")
        print("3. Devolver libro (por ISBN)")
        print("4. Mostrar stock total")
        print("5. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ")

        # Uso de MATCH/CASE
        match opcion:
            case "1":
                print("\n--- LIBROS DISPONIBLES ---")
                lista = inventario.listar_libros_disponibles()
                if lista:
                    for item in lista:
                        print(f"- {item}")
                else:
                    print("El inventario está vacío.")

            case "2":
                query = input("Título o ISBN del libro a alquilar: ")
                resultado = inventario.alquilar_copia(query)

                # Reemplazo de isinstance(): Se verifica si el resultado es un objeto Libro
                if type(resultado) is Libro:
                    print(f"➡️ ALQUILER EXITOSO: Se entregó '{resultado.titulo}'.")
                else:
                    print(resultado)

            case "3":
                isbn_devolver = input("ISBN del libro a devolver: ")
                print(inventario.devolver_copia(isbn_devolver))

            case "4":
                # Cálculo de stock total usando un bucle FOR simple
                total_stock = 0
                for libro in inventario.coleccion_libros:
                    total_stock = total_stock + libro.copias_disponibles

                print(f"\nStock total de copias en el inventario: {total_stock}")

            case "5":
                print("👋 Saliendo del sistema de inventario. ¡Hasta pronto!")

            case _:
                print("❌ Opción no válida. Intente de nuevo.")


# = BLOQUE DE PRUEBA (main function) =
def inicializar_inventario() -> Inventario:
    """Función para pre-cargar el inventario con datos para la prueba."""
    inventario = Inventario()

    # Prueba de ISBN válido e inválido
    l1 = Libro("POO con Python", "Alice C.", "1234567890123", 2)
    l2 = Libro("Bases de Datos SQL", "Bob D.", "9876543210987", 3)
    l3 = Libro("POO con Python", "Alice C.", "1234567890123", 1)

    print("\n--- INICIALIZANDO INVENTARIO ---")
    print(inventario.agregar_libro(l1))
    print(inventario.agregar_libro(l2))
    print(inventario.agregar_libro(l3))

    # Prueba de asignación de ISBN inválido
    l2.isbn = "9876543210XXX"
    print(f"ISBN de L2 después de intento fallido: {l2.isbn}")

    # Pre-ajuste de stock
    inventario.alquilar_copia("Bases de Datos SQL")
    inventario.alquilar_copia("Bases de Datos SQL")
    inventario.alquilar_copia("1234567890123")
    print("--------------------------------")

    return inventario


if __name__ == "__main__":
    biblioteca = inicializar_inventario()
    menu(biblioteca)
