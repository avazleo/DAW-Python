def buscar(lista, valor):
    if not lista:
        return False
    if lista[0] == valor:
        return True
    return buscar(lista[1:], valor)

def main():
    my_list = [10, 20, 30, 40, 50]
    value_to_find = 30
    if buscar(my_list, value_to_find):
        print(f"{value_to_find} is in the list.")
    else:
        print(f"{value_to_find} is not in the list.")

    value_to_find = 60
    if buscar(my_list, value_to_find):
        print(f"{value_to_find} is in the list.")
    else:
        print(f"{value_to_find} is not in the list.")

if __name__ == '__main__':
    main()