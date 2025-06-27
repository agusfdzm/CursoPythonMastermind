import os

def main():
    edadUsuario = int(input("Introduce tu edad: "))

    if edadUsuario <= 0 or edadUsuario >= 120:
        print("Edad no válida, saliendo del programa...\n")
        return
    elif edadUsuario < 18:
        print("No puedes acceder al programa\n")
        print("Saliendo...")
        return
    elif edadUsuario >= 18:
        print("Tu edad es válida")
        saludar()

def saludar():
    print("Tienes mas de 18 años y has accedido al programa")
    os.system("dir")

if __name__ == "__main__":
    main()
