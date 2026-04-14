import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse("productos.xml")
root = tree.getroot()
for producto in root.findall("producto"):
    nombre = producto.findtext("nombre", default="(sin nombre)")
    precio_txt = producto.findtext("precio", default="0")
    try:
        precio = float(precio_txt)
    except ValueError:
        print(f"Precio inválido en {nombre}: {precio_txt}. Se deja igual.")
        continue

nuevo_precio = round(precio * 1.10, 2)
producto.find("precio").text = f"{nuevo_precio:.2f}"
print(f"{nombre}: {precio:.2f} -> {nuevo_precio:.2f}")

xml_bytes = ET.tostring(root, encoding="utf-8")
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent="    ")
xml_pretty = "\n".join([line for line in xml_pretty.splitlines() if line.strip()])

with open("productos.xml", "w", encoding="utf-8") as f:
    f.write(xml_pretty)

