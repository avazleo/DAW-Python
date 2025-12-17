from typing import Protocol

class VehiculoProto(Protocol):
    @property
    def velocidad(self) -> float: ...
    def arrancar(self) -> None: ...
    def detener(self) -> None: ...
    def acelerar(self, n: float) -> None: ...
    def frenar(self, n: float) -> None: ...

class Patinete:
    def __init__(self) -> None:
        self._vel = 0.0
        self._on = False

    @property
    def velocidad(self) -> float:
        return self._vel

    def arrancar(self) -> None:
        self._on = True

    def detener(self) -> None:
        self._on = False
        self._vel = 0.0

    def acelerar(self, n: float) -> None:
        if self._on:
            self._vel += n

    def frenar(self, n: float) -> None:
        self._vel = max(0.0, self._vel - n)

def prueba_proto(v: VehiculoProto) -> None:
    v.arrancar()
    v.acelerar(12)
    v.frenar(5)
    print(v.velocidad)

if __name__ == "__main__":
    p = Patinete()
    prueba_proto(p)  # ✔️ Aunque Patinete NO hereda de VehiculoProto, “encaja” por estructura