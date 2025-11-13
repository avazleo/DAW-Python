def invertir(cadena):
    if len(cadena) <= 1:
        return cadena
    return invertir(cadena[1:]) + cadena[0]

def main():
    cadena = input('Enter a string: ')
    print(f"The reversed string is: {invertir(cadena)}")

if __name__ == '__main__':
    main()