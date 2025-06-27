import random

def listaStrings(lista):
    stringMasLargo = ""
    for item in lista:
        if len(item) > len(stringMasLargo):
            stringMasLargo = item

    print(f"El string mas largo de tu lista es {stringMasLargo}")

nombres = ["sol", "nube", "viento", "montañaaaa", "supercalifragilisticoespialidoso"]

def suma(numeros):
    listasNumeros = 0
    for num in numeros:
        listasNumeros += num

    print(listasNumeros)

numeros = [1, 2, 3, 4, 5]


def esImpar(num):
    if num % 2 != 0:
        return True
    else:
        return False
    

def estasSeguro():
    seguro = input("Estás seguro? [si/no]")
    seguro = seguro.lower()
    
    if seguro == "si":
        return True
    elif seguro == "no":
        return False
    else:
        print("Input no válido")


def adivinar(numAl):
    intento = int(input("Intenta adivinar el numero secreto (1-100): "))

    while intento != numAl:
        intento = int(input("Vuelve a intentarlo: "))
        
        if intento > 100:
            print("El numero comprende entre 1 y 100")
        elif intento < 0:
            print("El numero comprende entre 1 y 100")
        elif intento == numAl:
            print("OLEEEEE")    

numAl = random.randint(1, 100)


def listaCompra(compra):
    producto = ""
    while producto != "Q":
        producto = input("Añadir: (Q para salir) ")
        if producto in compra:
            print("Tu producto ya está en la lista")
        elif producto != "Q":
            compra.append(producto)

    print(f"Tu lista de la compra es: {compra}")

compra = []
listaCompra(compra)