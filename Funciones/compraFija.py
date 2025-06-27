from compraFuncional import preguntarUsuario

def main():
    productosValidos = ["Mostaza", "Pan", "Tarta"]
    
    inputUsuario = preguntarUsuario()

    while inputUsuario.lower() != "q":
        if inputUsuario in productosValidos:
            print("Tu producto es válido")

        elif inputUsuario == "LISTA":
            print(f"Los productos validos son: {productosValidos}")
        else:
            print("Tu producto no es valido")
        inputUsuario = preguntarUsuario()


if __name__ == "__main__":
    main()