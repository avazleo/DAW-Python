def suma_lista(lista):
    if not lista:
        return 0
    return lista[0] + suma_lista(lista[1:])

def main():
    # Example usage:
    my_list = [1, 2, 3, 4, 5]
    print(f"The sum of the list {my_list} elements is: {suma_lista(my_list)}")

if __name__ == '__main__':
    main()