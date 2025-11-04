def es_palindromo(palabra):
    return palabra.upper() == palabra.upper()[::-1]

def main():
    palabra = input("Ingresa una palabra: ")
    if es_palindromo(palabra):
        print(f"{palabra} es palindromo")
    else:
        print(f"{palabra} no es palindromo")

if __name__ == '__main__':
    main()