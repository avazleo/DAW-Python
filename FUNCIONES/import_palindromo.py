import palindromo as pal

def main():
    palabra = input("Enter a word: ")
    if pal.es_palindromo(palabra):
        print(f"{palabra} is a palindrome")
    else:
        print(f"{palabra} is not a palindrome")

if __name__ == '__main__':
    main()