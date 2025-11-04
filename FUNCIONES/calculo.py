def calculo(numero1, numero2, operacion):
    match operacion:
        case "+": return numero1 + numero2
        case "-": return numero1 - numero2
        case "*": return numero1 * numero2
        case "/": return numero1 / numero2
        case _ : return None

def main():
    numero1 = int(input("Ingresa un numero1: "))
    numero2 = int(input("Ingresa un numero2: "))
    operacion = input("Ingresa una operacion: ")
    resultado = calculo(numero1, numero2, operacion)
    if resultado == None:
        print("La operación no es valida")
    else:
        print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}")

if __name__ == "__main__":
    main()
