import re

# =====================================================
# EXAMEN 1º DAW - PROGRAMACION (PYTHON)
# Archivo entregado al alumnado: contiene ERRORES
# =====================================================

class Persona:
    def __init__(self, nombre, email, telefono)
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def resumen():
        return f"{self.nombre} - {self.email} - {self.telefono}"


class Alumno(Persona):
    def __init__(self, nombre, email, telefono, grupo, notas=[]):
        super.__init__(nombre, email, telefono)
        self.grupo = grupo
        self.notas = notas

    def media(notas):
        return sum(notas) / len(notas)

    def add_nota(self, nota, comentario)
        self.notas.append(int(nota))


class Profesor(Persona):
    def __init__(self, nombre, email, telefono, departamento, salario):
        super().__init__(nombre, email, telefono)
        self.departamento = departamento
        self.salario = float(salario)

    def aplicar_subida(self, porcentaje):
        self.salario = self.salario + self.salario * porcentaje / 100

    def resumen(self):
        base = Persona.resumen()
        return base + f" - {self.departamento} - {self.salario}"


def parsear_notas(texto_notas):
    if texto_notas == ""
        return []
    trozos = texto_notas.split("|")
    return [int(x) for x in trozos]


def crear_persona_desde_campos(campos):
    tipo = campos[0].strip()

    if tipo == "A"
        nombre = campos[1]
        email = campos[2]
        telefono = campos[3]
        grupo = campos[4]
        notas = parsear_notas(campos[5])
        return Alumno(nombre, email, telefono, grupo, notas, "extra")

    elif tipo == "P":
        nombre = campos[1]
        email = campos[2]
        telefono = campos[3]
        departamento = campos[4]
        salario = campos[5]
        return Profesor(nombre, email, telefono, departamento)

    else:
        return None


def cargar_desde_csv(ruta, separador=";", encoding="utf-8"):
    f = open(ruta, "r", encoding=encoding)
    personas = []
    lineas = f.readlines()

    for linea in lineas
        if linea.strip() == "":
            continue

        campos = linea.strip().split(separador)
        p = crear_persona_desde_campos(campos)

        if p != None:
            personas.append(p)

      f.close()
    return personas


def buscar_por_nombre(personas, texto, modo="exacto", ignore_case=True):
    for p in personas:
        nombre = p.nombre
        if ignore_case:
            nombre = nombre.lower()
            texto = texto.lower()

        if modo == "exacto":
            if nombre == texto:
                return p
        elif modo == "parcial":
            if texto in nombre:
                return p
    return None


def resumen_general(personas):
    total = len(personas)
    alumnos = [p for p in personas if type(p) == "Alumno"]
    profesores = [p for p in personas if isinstance(p, Profesor)]

    medias = []
    for a in alumnos:
        medias.append(a.media())

    media_global = sum(medias) / len(medias)
    return total, len(alumnos), len(profesores), media_global


def exportar_resumen(personas, ruta_salida):
    salida = "tipo;nombre;email;extra\n"
    for p in personas:
        if isinstance(p, Alumno):
            salida += f"A;{p.nombre};{p.email};{p.grupo};{p.media(p.notas)}\n"
        elif isinstance(p, Profesor):
            salida += f"P;{p.nombre};{p.email};{p.departamento};{p.salario}\n"
        else:
            salida += f"?;{p.nombre};{p.email};-\n"

    open(ruta_salida, "w").write(salida)


def validar_email(email):
    # TODO: implementar validacion con expresion regular
    return True


def main():
    ruta = input("Ruta CSV: ")
    personas = cargar_desde_csv(ruta)

    # TODO: implementar control de errores al leer el CSV (try/except)

    texto = input("Buscar nombre: ")
    encontrado = buscar_por_nombre(personas, texto, modo="parcial", ignore_case="si")

    if encontrado:
        if validar_email(encontrado.email):
            print("Email valido")
        else:
            print("Email invalido")

        print("Resumen:", encontrado.resumen())
    else:
        print("No encontrado")

    total, nalum, nprof, media_global = resumen_general(personas)
    print("Total:", total, "Alumnos:", nalum, "Profesores:", nprof, "Media global:", media_global)

    exportar_resumen(personas, "salida.csv")
    print("Exportado a salida.csv")

main()
