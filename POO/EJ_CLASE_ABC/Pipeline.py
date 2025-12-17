from abc import ABC, abstractmethod

class Pipeline(ABC):
    @abstractmethod
    def ejecutar(self) -> None:
        """Ejecuta el pipeline completo de datos."""
        ...

class PipelineCSV(Pipeline):
    def ejecutar(self) -> None:
        print("=== Pipeline CSV ===")
        print("Cargando datos desde CSV...")
        print("Procesando datos CSV...")
        print("Guardando resultados CSV...")
        print("=== Fin pipeline CSV ===\n")

class PipelineJSON(Pipeline):
    def ejecutar(self) -> None:
        print("=== Pipeline JSON ===")
        print("Cargando datos desde JSON...")
        print("Procesando datos JSON...")
        print("Guardando resultados JSON...")
        print("=== Fin pipeline JSON ===\n")

class PipelineAPI(Pipeline):
    def ejecutar(self) -> None:
        print("=== Pipeline API ===")
        print("Obteniendo datos desde API...")
        print("Procesando datos de la API...")
        print("Guardando resultados API...")
        print("=== Fin pipeline API ===\n")

# Ejemplo de uso
pipelines: list[Pipeline] = [PipelineCSV(), PipelineJSON(), PipelineAPI()]

for p in pipelines:
    p.ejecutar()