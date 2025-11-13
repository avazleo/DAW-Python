def suma_n(n):
    if n == 0:
        return 0
    return n + suma_n(n - 1)


def main():
    n = int(input('Enter a number: '))
    print(f"The sum of the first {n} numbers is {suma_n(n)}")


if __name__ == '__main__':
    main()