def fibonacciRecursivo(n):
    if n <= 1:
        return 1
    return fibonacciRecursivo(n-1) + fibonacciRecursivo(n-2)

def main():
    for a in range(10):
        print(fibonacciRecursivo(a))

if __name__ == "__main__":
    main()