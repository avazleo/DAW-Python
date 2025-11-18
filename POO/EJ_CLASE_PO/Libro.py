class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f'El titulo del libro es {self.titulo}, su autor es {self.autor} y es del año {self.anio}'

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor={self.autor}, anio={self.anio})"  # técnico

def main():
    libro = Libro("El Señor de los anillos", "JRR Tolkien", 1700)
    print(libro)
    print(str(libro))
    print(repr(libro))

if __name__ == "__main__":
    main()