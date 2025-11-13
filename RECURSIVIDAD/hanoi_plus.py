def mostrar_torres(A, B, C):
    """Muestra el estado actual de las tres torres."""
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")
    print("-" * 20)

def hanoi(n, origen, auxiliar, destino, torres):
    if n == 1:
        disco = torres[origen].pop()       # Quitar el disco superior del origen
        torres[destino].append(disco)      # Colocarlo en el destino
        print(f"Mueve disco {disco} de {origen} → {destino}")
        mostrar_torres(torres['A'], torres['B'], torres['C'])
        return

    # Mueve n-1 discos del origen al auxiliar
    hanoi(n - 1, origen, destino, auxiliar, torres)

    # Mueve el disco más grande al destino
    disco = torres[origen].pop()
    torres[destino].append(disco)
    print(f"Mueve disco {disco} de {origen} → {destino}")
    mostrar_torres(torres['A'], torres['B'], torres['C'])

    # Mueve los n-1 discos del auxiliar al destino
    hanoi(n - 1, auxiliar, origen, destino, torres)


# --- Ejemplo de uso ---
n = 3  # número de discos
torres = {
    'A': list(range(n, 0, -1)),  # origen
    'B': [],                     # auxiliar
    'C': []                      # destino
}

print("Estado inicial:")
mostrar_torres(torres['A'], torres['B'], torres['C'])

hanoi(n, 'A', 'B', 'C', torres)
print("¡Torres completadas! 🎉")