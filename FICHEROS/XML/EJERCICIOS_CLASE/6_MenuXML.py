import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

RUTA = "clientes.xml"
def guardar_pretty(tree: ET.ElementTree, ruta: str) -> None:
    xml_bytes = ET.tostring(tree.getroot(), encoding="utf-8")
    pretty = minidom.parseString(xml_bytes).toprettyxml(indent=" ")
    pretty = "\n".join([line for line in pretty.splitlines() if line.strip()])
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(pretty)

def cargar_o_crear(ruta: str) -> ET.ElementTree:
    """Carga clientes.xml o crea uno nuevo si no existe."""
    if not os.path.exists(ruta):
        root = ET.Element("clientes")
        tree = ET.ElementTree(root)
        guardar_pretty(tree, ruta)
        return tree
    return ET.parse(ruta)

def dni_existe(root: ET.Element, dni: str) -> bool:
    for cliente in root.findall("cliente"):
        if cliente.findtext("dni") == dni:
            return True
    return False

def listar_clientes(root: ET.Element) -> None:
    clientes = root.findall("cliente")
    if not clientes:
        print("No hay clientes.")
        return
    for c in clientes:
        print(f"- {c.findtext('dni')} | {c.findtext('nombre')} | {c.findtext('email')}")

def buscar_cliente(root: ET.Element, dni: str) -> ET.Element | None:
    for c in root.findall("cliente"):
        if c.findtext("dni") == dni:
            return c
    return None

def anadir_cliente(tree: ET.ElementTree) -> None:
    root = tree.getroot()
    dni = input("DNI: ").strip().upper()
    nombre = input("Nombre: ").strip()
    email = input("Email: ").strip()
    if not dni or not nombre or not email:
        print("Datos incompletos. No se añade.")
        return
    if dni_existe(root, dni):
        print("Ese DNI ya existe. No se añade.")
        return

    cliente = ET.SubElement(root, "cliente")
    ET.SubElement(cliente, "dni").text = dni
    ET.SubElement(cliente, "nombre").text = nombre
    ET.SubElement(cliente, "email").text = email
    guardar_pretty(tree, RUTA)
    print("Cliente añadido y guardado.")

def eliminar_cliente(tree: ET.ElementTree) -> None:
    root = tree.getroot()
    dni = input("DNI a eliminar: ").strip().upper()
    c = buscar_cliente(root, dni)
    if c is None:
        print("No existe ese DNI.")
        return
    root.remove(c)
    guardar_pretty(tree, RUTA)
    print("Cliente eliminado y guardado.")

def menu() -> None:
    try:
        tree = cargar_o_crear(RUTA)
    except ET.ParseError:
        print("ERROR: El XML está mal formado. Revisa clientes.xml.")
        return
    except Exception as e:
        print("ERROR al cargar el fichero:", e)
        return

    while True:
        print("\n--- MENÚ CLIENTES ---")
        print("1) Añadir cliente")
        print("2) Listar clientes")
        print("3) Buscar cliente por DNI")
        print("4) Eliminar cliente")
        print("5) Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            anadir_cliente(tree)
        elif opcion == "2":
            listar_clientes(tree.getroot())
        elif opcion == "3":
            dni = input("DNI a buscar: ").strip().upper()
            c = buscar_cliente(tree.getroot(), dni)
            if c is None:
                print("No encontrado.")
            else:
                print(f"Encontrado: {c.findtext('dni')} | {c.findtext('nombre')} | {c.findtext('email')}")
        elif opcion == "4":
            eliminar_cliente(tree)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
         print("Opción inválida.")

if __name__ == "__main__":
    menu()