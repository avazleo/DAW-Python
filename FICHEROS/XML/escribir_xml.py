import xml.etree.ElementTree as ET
from xml.dom import minidom

# 1️⃣ Crear el elemento raíz
root = ET.Element("libreria")

# 2️⃣ Crear primer libro
libro1 = ET.SubElement(root, "libro")
ET.SubElement(libro1, "titulo").text = "Don Quijote"
ET.SubElement(libro1, "autor").text = "Miguel de Cervantes"
ET.SubElement(libro1, "precio").text = "19.95"

# 3️⃣ Crear segundo libro
libro2 = ET.SubElement(root, "libro")
ET.SubElement(libro2, "titulo").text = "1984"
ET.SubElement(libro2, "autor").text = "George Orwell"
ET.SubElement(libro2, "precio").text = "15.50"

# 4️⃣ Convertir a árbol
tree = ET.ElementTree(root)

# 5️⃣ Guardar con formato bonito (indentado)
xml_bytes = ET.tostring(root, encoding="utf-8")
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent="    ")

with open("libros.xml", "w", encoding="utf-8") as f:
    f.write(xml_pretty)

print("Fichero libros.xml creado correctamente.")
