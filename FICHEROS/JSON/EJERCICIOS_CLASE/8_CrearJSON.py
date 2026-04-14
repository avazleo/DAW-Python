import json

usuarios = [
    {"id": 1, "nombre": "Ana", "email": "ana@correo.com"},
    {"id": 2, "nombre": "Luis", "email": "luis@correo.com"},
    {"id": 3, "nombre": "María", "email": "maria@correo.com"},
]
with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, ensure_ascii=False, indent=4)