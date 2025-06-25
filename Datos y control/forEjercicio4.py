numero = int(input("Introduce un numero a la lista: "))

contador = 0

listaNum = []

listaNum.append(numero)

while contador < 4:
    numero = int(input("Introduce otro numero a la lista: "))
    listaNum.append(numero)
    contador += 1

pequeño = min(listaNum)
grande = max(listaNum)

print(f"""
El numero mas grande es: {grande}\n
El numero mas pequeño es: {pequeño}\n
""")