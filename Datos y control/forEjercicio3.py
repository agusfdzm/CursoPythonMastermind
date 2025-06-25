numUsuario = int(input("Introduce un numero: "))

for i in range(1, 11):
    mult = numUsuario * i

    if mult % 2 == 0:
        print(f"{numUsuario} * {i} = {mult}")