def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

def main():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Please enter a positive integer.")
    else:
        print(f"The number of digits in {n} is: {contar_digitos(n)}")

if __name__ == '__main__':
    main()