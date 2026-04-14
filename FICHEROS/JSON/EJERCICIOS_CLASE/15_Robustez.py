import csv
import json

entrada = input("Fichero de entrada a convertir (.csv/.json): ").strip()
salida = input("Fichero de salida (.csv/.json): ").strip()
try:
    if entrada.lower().endswith(".csv") and salida.lower().endswith(".json"):
        # CSV -> JSON
        with open(entrada, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            datos = list(reader)

        with open(salida, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=4)

    elif entrada.lower().endswith(".json") and salida.lower().endswith(".csv"):
        # JSON -> CSV
        with open(entrada, "r", encoding="utf-8") as f:
            datos = json.load(f)

        if not isinstance(datos, list):
            raise ValueError("El JSON de entrada debe ser una lista de objetos")

        # Cabeceras: unión de claves
        claves = set()
        for item in datos:
            if isinstance(item, dict):
                claves.update(item.keys())

        fieldnames = sorted(claves)

        with open(salida, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in datos:
                if isinstance(item, dict):
                    writer.writerow(item)

    else:
        raise ValueError("Extensiones no soportadas. Usa .csv→.json o .json→.csv")

    print("Conversión realizada con éxito.")

except FileNotFoundError:
    print("Error: fichero de entrada no encontrado")
except PermissionError:
    print("Error: permisos insuficientes para leer/escribir")
except json.JSONDecodeError:
    print("Error: JSON inválido (mal formado)")
except ValueError as e:
    print("Error:", e)
except OSError as e:
    print("Error del sistema:", e)