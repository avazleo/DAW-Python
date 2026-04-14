import json

try:
    with open("usuarios.json", "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    print("JSON leído correctamente")
except FileNotFoundError:
    print("Error: usuarios.json no existe")
except json.JSONDecodeError:
    print("Error: el fichero JSON está corrupto o no tiene un formato válido")