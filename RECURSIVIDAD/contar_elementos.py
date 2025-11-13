def contar_elementos(lista):
    if not lista:
        return 0
    return 1 + contar_elementos(lista[1:])

def main():
    # Example usage:
    my_list = [10, 20, 30, 40, 50, 60]
    print(f"The number of elements in the list {my_list} is: {contar_elementos(my_list)}")

if __name__ == '__main__':
    main()