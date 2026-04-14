import json

with open("usuarios.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

for u in usuarios:
    print(f"[{u['id']}] {u['nombre']} <{u['email']}>")