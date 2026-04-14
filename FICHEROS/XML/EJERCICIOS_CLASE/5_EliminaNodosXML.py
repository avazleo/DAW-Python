import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse("tienda.xml")
root = tree.getroot()
eliminados = 0
# Importante: iterar sobre una lista copia para poder borrar sin problemas
for producto in list(root.findall("producto")):
    if producto.get("stock") == "0":
        root.remove(producto)
        eliminados += 1

xml_bytes = ET.tostring(root, encoding="utf-8")
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent="    ")
xml_pretty = "\n".join([line for line in xml_pretty.splitlines() if line.strip()])

with open("tienda.xml", "w", encoding="utf-8") as f:
    f.write(xml_pretty)

print("Productos eliminados:", eliminados)