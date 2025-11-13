def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

def main():
    base = int(input('Enter the base: '))
    exponente = int(input('Enter the exponent: '))
    print(f"{base} raised to the power of {exponente} is {potencia(base, exponente)}")

if __name__ == '__main__':
    main()