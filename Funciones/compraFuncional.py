def guardarArchivo(lista):
    with open("miListaCompra.txt", "w") as archivo:
        for i in lista:
            archivo.write(i + "\n")


def preguntarUsuario():
    return input("Introduce un producto (Q para salir): ")


def main():
    listaCompra = []
    inputUsuario = preguntarUsuario()

    if inputUsuario == "Q" or inputUsuario == "q":
        print("Saliendo...")
    else:
        print(f"Añadiendo {inputUsuario} a la lista")
        listaCompra.append(inputUsuario)

        while inputUsuario != "Q" and inputUsuario != "q":
            inputUsuario = preguntarUsuario()
            
            if inputUsuario != "Q" and inputUsuario != "q":
                listaCompra.append(inputUsuario)

        guardarArchivo(listaCompra)
        print("Lista guardadada...")


if __name__ == "__main__":
    main()