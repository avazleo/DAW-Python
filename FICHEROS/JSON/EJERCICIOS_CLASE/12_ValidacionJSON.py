import json

CLAVES = {"id", "nombre", "email"}
with open("usuarios.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

usuarios_validos = []
if not isinstance(datos, list):
    print("Aviso: el JSON no contiene una lista")
else:
    for item in datos:
        if not isinstance(item, dict):
            print("Aviso: elemento no es objeto JSON:", item)
            continue
        if not CLAVES.issubset(item.keys()):
            print("Aviso: faltan claves en usuario:", item)
            continue
        usuarios_validos.append(item)

print("Usuarios válidos:", len(usuarios_validos))