
# =====================================================
# SOLUCIÓN VERSION SIMPLE v2 (1º DAW)
# - Sin dataclasses / typing / __future__
# - Añade comprobaciones de longitud de línea y campos obligatorios
# - Detecta líneas incompletas (sin grupo / sin salario, etc.)
# =====================================================

import csv
import re


class Persona:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def resumen(self):
        return f"{self.nombre} - {self.email} - {self.telefono}"


class Alumno(Persona):
    def __init__(self, nombre, email, telefono, grupo, notas=None):
        super().__init__(nombre, email, telefono)
        self.grupo = grupo
        self.notas = notas if notas is not None else []

    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def add_nota(self, nota):
        self.notas.append(int(nota))

    def resumen(self):
        return super().resumen() + f" - {self.grupo} - media={self.media():.2f}"


class Profesor(Persona):
    def __init__(self, nombre, email, telefono, departamento, salario):
        super().__init__(nombre, email, telefono)
        self.departamento = departamento
        self.salario = float(salario)

    def aplicar_subida(self, porcentaje):
        self.salario += self.salario * porcentaje / 100

    def resumen(self):
        return super().resumen() + f" - {self.departamento} - salario={self.salario:.2f}"


def validar_email(email):
    patron = r"^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.fullmatch(patron, email.strip()) is not None


def parsear_notas(texto_notas):
    texto_notas = texto_notas.strip()
    if texto_notas == "":
        return []

    trozos = texto_notas.split("|")
    notas = []

    for t in trozos:
        t = t.strip()
        try:
            n = int(t)
        except ValueError:
            raise ValueError(f"Nota invalida (no numerica): {t}")

        if not (0 <= n <= 10):
            raise ValueError(f"Nota fuera de rango 0..10: {n}")

        notas.append(n)

    return notas


def crear_persona_desde_campos(campos):
    # Campos comunes obligatorios: tipo, nombre, email, telefono
    if len(campos) < 4:
        raise ValueError("Linea incompleta: faltan campos comunes (tipo,nombre,email,teléfono)")

    tipo = campos[0].strip()
    nombre = campos[1].strip()
    email = campos[2].strip()
    telefono = campos[3].strip()

    if tipo == "A":
        # Alumno: grupo, notas
        if len(campos) < 6:
            raise ValueError("Alumno incompleto: faltan grupo y/o notas")
        grupo = campos[4].strip()
        if grupo == "":
            raise ValueError("Alumno incompleto: grupo vacío")
        notas = parsear_notas(campos[5])
        return Alumno(nombre, email, telefono, grupo, notas)

    elif tipo == "P":
        # Profesor: departamento, salario
        if len(campos) < 6:
            raise ValueError("Profesor incompleto: faltan departamento y/o salario")
        departamento = campos[4].strip()
        if departamento == "":
            raise ValueError("Profesor incompleto: departamento vacío")
        salario_txt = campos[5].strip()
        if salario_txt == "":
            raise ValueError("Profesor incompleto: salario vacío")
        salario = float(salario_txt)
        return Profesor(nombre, email, telefono, departamento, salario)

    else:
        raise ValueError("Tipo desconocido")


def cargar_desde_csv(ruta):
    personas = []

    try:
        with open(ruta, "r", encoding="utf-8", newline="") as f:
            lector = csv.reader(f)
            for num_linea, fila in enumerate(lector, start=1):
                # saltar líneas vacías
                if not fila or all(c.strip() == "" for c in fila):
                    continue

                try:
                    persona = crear_persona_desde_campos(fila)
                    if not validar_email(persona.email):
                        print(f"[AVISO] Email invalido en linea {num_linea}: {persona.email}")
                    personas.append(persona)
                except Exception as e:
                    print(f"[ERROR] Linea {num_linea}: {e}")

    except FileNotFoundError:
        print("El fichero no existe.")
    except Exception as e:
        print("Error al abrir el fichero:", e)

    return personas


def exportar_resumen(personas, ruta_salida):
    with open(ruta_salida, "w", encoding="utf-8") as f:
        for p in personas:
            f.write(p.resumen() + "\n")


def buscar_por_nombre(personas, texto, modo="exacto", ignore_case=True):
    texto = texto.strip()
    if ignore_case:
        texto = texto.lower()

    for p in personas:
        nombre = p.nombre.strip()
        if ignore_case:
            nombre = nombre.lower()

        if modo == "exacto" and nombre == texto:
            return p
        if modo == "parcial" and texto in nombre:
            return p

    return None


def resumen_general(personas):
    alumnos = []
    profesores = []

    for p in personas:
        if isinstance(p, Alumno):
            alumnos.append(p)
        elif isinstance(p, Profesor):
            profesores.append(p)

    medias = [a.media() for a in alumnos]
    media_global = sum(medias) / len(medias) if len(medias) > 0 else 0

    return len(personas), len(alumnos), len(profesores), media_global


def main():
    ruta = input("Ruta CSV: ").strip()
    personas = cargar_desde_csv(ruta)

    texto = input("Buscar nombre: ").strip()
    encontrado = buscar_por_nombre(personas, texto, modo="parcial", ignore_case=True)

    if encontrado:
        print("Email valido" if validar_email(encontrado.email) else "Email invalido")
        print(encontrado.resumen())
    else:
        print("No encontrado")

    total, nalum, nprof, media = resumen_general(personas)
    print(f"Total: {total} | Alumnos: {nalum} | Profesores: {nprof} | Media global: {media:.2f}")

    exportar_resumen(personas, "salida.txt")
    print("Resumen exportado a salida.txt")


if __name__ == "__main__":
    main()
