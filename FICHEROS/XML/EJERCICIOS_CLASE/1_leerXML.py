import xml.etree.ElementTree as ET

tree = ET.parse("alumnos.xml")
root = tree.getroot()
total = 0

for alumno in root.findall("alumno"):
    nombre = alumno.findtext("nombre")
    edad = alumno.findtext("edad")
    print(f"{nombre} - {edad} años")
    total += 1

print("Total alumnos/as:", total)