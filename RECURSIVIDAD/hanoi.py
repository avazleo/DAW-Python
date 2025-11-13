def hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Move disc {origen} → {destino}")
        return

    hanoi(n - 1, origen, destino, auxiliar)
    print(f"Move disc {origen} → {destino}")
    hanoi(n - 1, auxiliar, origen, destino)

def main():
    # Ejemplo: mover 3 discos desde la torre A hasta la C usando la B como auxiliar
    hanoi(3, 'A', 'B', 'C')

main()
