def fib():
    maxNum = int(input("Introduce cuántos números de la secuencia quieres mostrar: "))

    a = 0
    b = 1

    for i in range(maxNum):
        print(a)
        siguiente = a + b
        a = b
        b = siguiente

fib()