def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    n = int(input("Enter a number: "))
    if n < 0:
        print("Fibonacci sequence is not defined for negative numbers")
    else:
        print(f"The {n}-th Fibonacci number is: {fibonacci(n)}")

if __name__ == '__main__':
    main()