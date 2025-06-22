os = input("¿Prefieres iOS o Android? ")

os = os.lower()

if os == "ios":
    dinero = input("¿Tienes dinero? ")

    dinero = dinero.lower()

    if dinero == "si":
        print("Cómprate el iPhone Ultra Pro Max")
    elif dinero == "no":
        print("Cómprate un iPhone de segunda mano")
    else:
        print("Opción no válida")
elif os == "android":
    dinero = input("¿Tienes dinero? ")
    dinero = dinero.lower()

    if dinero == "no":
        print("Cómprate un Android chino de 100€")
    elif dinero == "si":
        camara = input("¿Te importa la cámara? ")
        camara = camara.lower()

        if camara == "si":
            print("Cómprate un Google Pixel Supercamara")
        elif camara == "no":
            print("Android calidad-precio")
        else:
            print("Opción no válida")
    else:
        print("Opción no válida")
else:
    print("Opción no válida")