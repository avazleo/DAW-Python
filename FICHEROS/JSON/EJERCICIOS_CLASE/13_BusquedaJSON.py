import json

email_buscar = input("Email a buscar: ").strip().lower()
with open("usuarios.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

encontrado = None
for u in usuarios:
    if str(u.get("email", "")).strip().lower() == email_buscar:
        encontrado = u
        break
if encontrado is not None:
    print("Encontrado:", encontrado)
else:
    print("No se encontró el email")