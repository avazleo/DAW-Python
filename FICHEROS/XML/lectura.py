import xml.etree.ElementTree as ET

XML_FILE = "libros.xml"

tree = ET.parse(XML_FILE)  # creamos árbol XML (ElementTree)
root = tree.getroot()  # obtenemos nodo raíz

print(f"Etiqueta nodo raíz: {root.tag}\n")

# Leemos los elementos usando ciclos
for book in root:
    print(f"Nodo etiqueta: {book.tag}, atributos: {book.attrib}:")
    for child in book:
        print(f"- {child.tag}: {child.text}")
    print()