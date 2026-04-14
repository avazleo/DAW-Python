import xml.etree.ElementTree as ET
from xml.dom import minidom

def mostrar_por_departamento(root: ET.Element, departamento: str) -> None:
    print(f"Empleados del departamento {departamento}:")
    for emp in root.findall("empleado"):
        if emp.get("departamento") == departamento:
            nombre = emp.findtext("nombre")
            salario = emp.findtext("salario")
            print(f" - {nombre} ({salario}€) [id={emp.get('id')}]")

tree = ET.parse("empleados.xml")
root = tree.getroot()
# 1) Mostrar IT
mostrar_por_departamento(root, "IT")
# 2) Añadir nuevo empleado
nuevo = ET.SubElement(root, "empleado", attrib={"id": "3", "departamento": "IT"})
ET.SubElement(nuevo, "nombre").text = "Marta"
ET.SubElement(nuevo, "salario").text = "2100"
# 3) Volver a mostrar IT (ya aparece Marta)
mostrar_por_departamento(root, "IT")
# 4) Guardar cambios
xml_bytes = ET.tostring(root, encoding="utf-8")
xml_pretty = minidom.parseString(xml_bytes).toprettyxml(indent="    ")
xml_pretty = "\n".join([line for line in xml_pretty.splitlines() if line.strip()])

with open("empleados.xml", "w", encoding="utf-8") as f:
    f.write(xml_pretty)

