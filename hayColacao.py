hayColacao = input("¿Hay colacao? (S/N) ")

if hayColacao == "S":
    print("Iré a la nevera a ver si hay leche...")
    hayLeche = input("¿Y hay leche? (S/N) ")

    if hayLeche == "S":
        print("¡Bien! Ya puedo preparar mi colacao.")
    elif hayLeche == "N":
        print("No me puedo hacer el colacao... Tendré que ir a comprar leche.")
    else:
        print("Opción no válida")
elif hayColacao == "N":
    print("Tendré que ir a comprar colacao...")
else:
    print("Opción no válida")

if hayColacao == "S" and hayLeche == "S":
    print("Delicioso el colacao")