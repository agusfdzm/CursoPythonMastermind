listaCompra = []

print("Lista de la compra\n")

añadir = input("¿Que deseas comprar? [Q] para salir: ")

listaCompra.append(añadir)

while añadir != "Q":

    añadir = input("¿Que deseas comprar? [Q] para salir: ")

    if añadir in listaCompra:
        print("Tu producto no se añadirá porque ya está en la lista")
    else:
        listaCompra.append(añadir)

print(f"Tu lista de la compra es: {listaCompra}")