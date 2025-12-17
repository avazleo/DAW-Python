from typing import Protocol, runtime_checkable, Any

@runtime_checkable
class Plugin(Protocol):
    @property
    def nombre(self) -> str: ...
    def inicializar(self) -> None: ...
    def ejecutar(self, datos: Any) -> Any: ...

class PluginEmail:
    def __init__(self):
        self._nombre = "EmailPlugin"

    @property
    def nombre(self) -> str:
        return self._nombre

    def inicializar(self):
        print(f"[{self.nombre}] Inicializando sistema de correo...")

    def ejecutar(self, datos):
        print(f"[{self.nombre}] Enviando correo a {datos}")
        return True


class PluginBackup:
    def __init__(self):
        self._nombre = "BackupPlugin"

    @property
    def nombre(self) -> str:
        return self._nombre

    def inicializar(self):
        print(f"[{self.nombre}] Preparando copia de seguridad...")

    def ejecutar(self, datos):
        print(f"[{self.nombre}] Guardando archivos en {datos}")
        return True

def cargar_plugin(plugin_obj):
    if not isinstance(plugin_obj, Plugin):
        raise TypeError(f"❌ El objeto {plugin_obj.__class__.__name__} no cumple la interfaz Plugin")

    print(f"✅ Cargando plugin: {plugin_obj.nombre}")
    plugin_obj.inicializar()
    plugin_obj.ejecutar("datos_de_prueba")

if __name__ == "__main__":
    email = PluginEmail()
    backup = PluginBackup()

    cargar_plugin(email)
    cargar_plugin(backup)

    class Malo:
        def ejecutar(self, datos): pass  # Falta `nombre` e `inicializar`

    cargar_plugin(Malo())  # ❌ Error
