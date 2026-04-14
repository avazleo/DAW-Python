import xml.etree.ElementTree as ET
from xml.dom import minidom


# 1) Crear raíz
root = ET.Element("libreria")
# 2) Datos (podrían venir de input(), una lista, etc.)
libros = [
    {"titulo": "Don Quijote", "autor": "Miguel de Cervantes", "precio": "19.95"},
    {"titulo": "1984", "autor": "George Orwell", "precio": "15.50"},
    {"titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "precio": "12.00"},
]
# 3) Construir nodos
for l in libros:
    libro = ET.SubElement(root, "libro")
    ET.SubElement(libro, "titulo").text = l["titulo"]
    ET.SubElement(libro, "autor").text = l["autor"]
    ET.SubElement(libro, "precio").text = l["precio"]
# 4) Guardar
tree = ET.ElementTree(root)

# 5️⃣ Guardar con formato bonito (indentado)
xml_bytes = ET.tostring(root, encoding="utf-8")
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent="    ")

with open("libros.xml", "w", encoding="utf-8") as f:
    f.write(xml_pretty)

print("Creado libros.xml")