import json

with open("usuarios.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

nuevo_id = max((u.get("id", 0) for u in usuarios if isinstance(u, dict)), default=0) + 1
nombre = input("Nombre: ")
email = input("Email: ")
usuarios.append({"id": nuevo_id, "nombre": nombre, "email": email})

with open("usuarios.json", "w", encoding="utf-8") as f:
    json.dump(usuarios, f, ensure_ascii=False, indent=4)