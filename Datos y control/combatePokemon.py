import random
import os

vidaPikachu = 80
vidaSquirtle = 90

vidaPikachuInicial = 80
vidaSquirtleInicial = 90

while vidaPikachu > 0 and vidaSquirtle > 0:
    print("EL COMBATE HA COMENZADO")

    print("""
    1. Placaje (10 de daño)
    2. Pistola agua (12 de daño)
    3. Burbuja (9 de daño)
    """)

    ataque = int(input("Que ataque quieres hacer? "))

    if ataque == 1:
        print("Placaje realizado. Pikachu ha perdido 10 de vida")
        vidaPikachu = vidaPikachu - 10
    elif ataque == 2:
        print("Pistola agua realizada. Pikachu ha perdido 12 de vida")
        vidaPikachu = vidaPikachu - 12
    elif ataque == 3:
        print("Burbuja realizada. Pikachu ha perdido 9 de vida")
        vidaPikachu = vidaPikachu - 9
    else:
        print("Ataque no válido")

    porcentajeVidaPikachu = int(vidaPikachu / vidaPikachuInicial * 100)
    porcentajeVidaSquirtle = int(vidaSquirtle / vidaSquirtleInicial * 100)

    print("Vida actual de Pikachu: {} {}".format(vidaPikachu, "#" * porcentajeVidaPikachu ))
    print(f"Vida actual de Squirtle: {vidaSquirtle}")


    input("Enter para continuar...\n\n")
    os.system("cls")

    ataqueAleatorio = random.randint(1, 2)

    if ataqueAleatorio == 1:
        print("Bola voltio realizada. Squirtle ha perdido  10 de vida")
        vidaSquirtle = vidaSquirtle - 10
    elif ataqueAleatorio == 2:
        print("Onda trueno realizada. Squirtle ha perdido 11 de vida")
        vidaSquirtle = vidaSquirtle - 11

    porcentajeVidaPikachu = int(vidaPikachu / vidaPikachuInicial * 100)
    porcentajeVidaSquirtle = int(vidaSquirtle / vidaSquirtleInicial * 100)

    print(f"Vida actual de Pikachu: {vidaPikachu}")
    print(f"Vida actual de Squirtle: {vidaSquirtle}")

    input("Enter para continuar...\n\n")
    os.system("cls")
    

if vidaPikachu <= 0:
    print("¡Squirtle ha ganado el combate!")
elif vidaSquirtle <= 0:
    print("¡Pikachu ha ganado el combate!")
