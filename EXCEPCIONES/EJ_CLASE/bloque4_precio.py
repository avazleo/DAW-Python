def validar_precio(precio):
    if precio < 0:
        return precio
    raise ValueError("El precio no puede ser negativo")