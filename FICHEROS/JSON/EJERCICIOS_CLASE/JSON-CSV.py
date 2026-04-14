import csv
import json

with open("usuarios.json", "r", encoding="utf-8") as f:
    usuarios = json.load(f)

with open("usuarios.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "nombre", "email"])
    writer.writeheader()
    for u in usuarios:
        if isinstance(u, dict):
            writer.writerow({
                "id": u.get("id"),
                "nombre": u.get("nombre"),
                "email": u.get("email"),
            })